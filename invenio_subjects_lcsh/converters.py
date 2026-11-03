# -*- coding: utf-8 -*-
#
# Copyright (C) 2024-2026 Northwestern University.
#
# invenio-subjects-lcsh is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Generic conversion functionality."""

from .scheme import LCSHScheme


def to_rdm_id(id_of_subject):
    """Convert LCSH id to RDM LCSH id."""
    return id_of_subject.replace("http://", "https://")


class LCSHRDMConverter:
    """Convert LCSH term into RDM subjects dict."""

    def __init__(self, internal_entries):
        """Constructor.

        Args:
            topic (dict - internal entry shape): internal LCSH entry
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
