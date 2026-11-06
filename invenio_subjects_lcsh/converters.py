#
# Copyright (C) 2024-2026 Northwestern University.
#
# invenio-subjects-lcsh is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Generic conversion functionality."""

from itertools import chain, takewhile

from .scheme import LCSHScheme, identify_scheme


def to_rdm_id(id_of_subject):
    """Convert LCSH id to RDM LCSH id."""
    return id_of_subject.replace("http://", "https://")


class LCSHRDMConverter:
    """Convert LCSH term into RDM subjects dict."""

    def __init__(self, internal_entries):
        """Constructor.

        Args:
            internal_entries (dict - internal entry shape): internal LCSH entry
        """
        self.internal_entries = internal_entries
        self.lcsh = LCSHScheme()

    def convert_entry(self, entry):
        """Extract relevant dict from LCSH mads-rdf json-ld dict."""
        return {
            "id": to_rdm_id(entry["id"]),
            "scheme": self.lcsh.name,
            "subject": entry["label"],
        }

    def iter_rdm_subjects(self):
        """Iterator over converted entries."""
        yield from (
            self.convert_entry(entry) for entry in self.internal_entries
        )


class LCSHReplacementConverter:
    """Convert internal entries into replacement entries."""

    def __init__(self, entries_deprecated, labelling_sources):
        """Constructor.

        Args:
            entries_deprecated (dict - internal entry shape): internal LCSH
                                                              entry
            labelling_sources (iterable[dict - internal entry shape]):
                iterable internal LCSH entries for labelling purposes
        """
        self._entries_deprecated = entries_deprecated
        self.lcsh = LCSHScheme()
        self._subjects_rdm = chain.from_iterable(labelling_sources)

    def _to_unlabelled_replacement_entry(self, entry):
        """Convert entry.

        Args:
            entry (dict - internal entry shape): read LCSH

        Returns:
            dict - replacement shape: replacement dict
        """
        return {
            "time": entry["deprecated"]["time"],
            "id": to_rdm_id(entry["id"]),
            "subject": entry["label"],
            "new_id": "\n".join(
                [to_rdm_id(rid) for rid in entry["deprecated"]["replacements"]]
            ),
            "new_scheme": "\n".join(
                [
                    identify_scheme(to_rdm_id(rid))
                    for rid in entry["deprecated"]["replacements"]
                ]
            ),
            "new_subject": "",  # don't bother in this pass, enhanced later
            "notes": entry["deprecated"]["note"],
        }

    def _assign_subject(self, subject, id_to_label_mapping):

        id_of_subject = subject["id"]

        if id_of_subject not in id_to_label_mapping:
            return  # do nothing

        id_to_label_mapping[id_of_subject] = subject["subject"]

    def _get_id_to_label_mapping(self, replacements_list):

        # 1) Get ids of all recommended replacements
        iterable_of_list_of_replacement_ids = (
            replacement["new_id"].splitlines()
            for replacement in replacements_list
        )
        # flatten out iter[list[replacement_id]] to iter[replacement_id]
        replacement_ids = chain.from_iterable(
            iterable_of_list_of_replacement_ids
        )
        id_to_label = {rid: "" for rid in replacement_ids}

        # 2) Fill id_to_label
        [
            self._assign_subject(subject, id_to_label)
            for subject in takewhile(
                # while not all ids have a label
                lambda e: not all(id_to_label.values()),
                self._subjects_rdm,
            )
        ]

        return id_to_label

    def _label_new_subjects(self, replacement_entry, id_to_label):
        """Fill in the new subject field.

        Args:
            replacement_entry (_type_): _description_
            id_to_label (_type_): _description_

        Returns:
            replacement_entry (dict - replacement entry shape): with subject

        """
        subjects = [
            # fallback to empty string in case no labels were found
            id_to_label.get(new_id, "")
            for new_id in replacement_entry["new_id"].splitlines()
        ]
        replacement_entry["new_subject"] = "\n".join(subjects)
        return replacement_entry

    def iter_replacements(self):
        """Iterator over replacemnt entries.

        Replacement dict has this shape:
            {
                "time": ...,
                "id": ...,
                "subject": ...,
                "new_id": ...,
                "new_subject": ...,
                "notes": ...
            }

        Yields:
            dict - replacement entry shape: replacement dict
        """
        # Keep as a list to iterate over multiple times
        replacements_list = [
            self._to_unlabelled_replacement_entry(e)
            for e in self._entries_deprecated
        ]

        id_to_label = self._get_id_to_label_mapping(replacements_list)

        yield from (
            self._label_new_subjects(r, id_to_label)
            for r in replacements_list
        )
