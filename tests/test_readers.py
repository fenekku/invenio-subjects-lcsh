#
# Copyright (C) 2026 Northwestern University.
#
# invenio-subjects-lcsh is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Test readers."""

from pathlib import Path

from invenio_subjects_lcsh.filters import valid_heading_filter
from invenio_subjects_lcsh.readers import LCSHMadsRdfJsonLdReader


def test_mads_rdf_json_ld_reader(valid_internal_entries):
    filepath = Path(__file__).parent / "data" / "fake_lcsh.madsrdf.jsonld"

    reader = LCSHMadsRdfJsonLdReader(
        filepath,
        filter=valid_heading_filter,
    )
    entries = list(reader.iter_internal_entries())

    assert valid_internal_entries == entries
