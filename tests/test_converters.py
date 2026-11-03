# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 Northwestern University.
#
# invenio-subjects-lcsh is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


from invenio_subjects_lcsh.converters import LCSHRDMConverter


def test_rdm_converter(valid_internal_entries):
    converter = LCSHRDMConverter(valid_internal_entries)

    dicts_of_lcsh_terms = [d for d in converter.iter_rdm_subjects()]

    expected = [
        {
            "id": "https://id.loc.gov/authorities/subjects/sh2006005259",
            "scheme": "LCSH",
            "subject": "Video games industry",
        },
        {
            "id": "https://id.loc.gov/authorities/subjects/sh2021004026",
            "scheme": "LCSH",
            "subject": "Child internment camp inmates",
        },
        {
            "id": "https://id.loc.gov/authorities/subjects/sh2021004027",
            "scheme": "LCSH",
            "subject": "Child Nazi concentration camp inmates",
        },
        {
            "id": "https://id.loc.gov/authorities/subjects/sh85143203",
            "scheme": "LCSH",
            "subject": "Video games--Law and legislation",
        },
        {
            "id": "https://id.loc.gov/authorities/subjects/sh2022001319",
            "scheme": "LCSH",
            "subject": "Evangelisch Luthersche Kerk (Netherlands)--Relations--Nederlandse Hervormde Kerk",  # noqa
        },
    ]
    assert expected == dicts_of_lcsh_terms
