#
# Copyright (C) 2026 Northwestern University.
#
# invenio-subjects-lcsh is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Conftest."""

import pytest


@pytest.fixture()
def valid_internal_entries():
    """Fixture for valid LCSH internal entries."""
    return [
        {
            "id": "http://id.loc.gov/authorities/subjects/sh2006005259",
            "label": "Video games industry",
            "deprecated": {
                "status": False,
                "note": "",
                "replacements": [],
                "at": None,
            },
            "collections": [
                "http://id.loc.gov/authorities/subjects/collection_LCSHAuthorizedHeadings",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_LCSH_General",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_SubdivideGeographically",  # noqa
            ],
        },
        {
            "id": "http://id.loc.gov/authorities/subjects/sh2021004026",
            "label": "Child internment camp inmates",
            "deprecated": {
                "status": False,
                "note": "",
                "replacements": [],
                "at": None,
            },
            "collections": [
                "http://id.loc.gov/authorities/subjects/collection_LCSHAuthorizedHeadings",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_LCSH_General",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_SubdivideGeographically",  # noqa
            ],
        },
        {
            "id": "http://id.loc.gov/authorities/subjects/sh2021004027",
            "label": "Child Nazi concentration camp inmates",
            "deprecated": {
                "status": False,
                "note": "",
                "replacements": [],
                "at": None,
            },
            "collections": [
                "http://id.loc.gov/authorities/subjects/collection_LCSHAuthorizedHeadings",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_LCSH_General",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_SubdivideGeographically",  # noqa
            ],
        },
        {
            "id": "http://id.loc.gov/authorities/subjects/sh85143203",
            "label": "Video games--Law and legislation",
            "deprecated": {
                "status": False,
                "note": "",
                "replacements": [],
                "at": None,
            },
            "collections": [
                "http://id.loc.gov/authorities/subjects/collection_LCSHAuthorizedHeadings",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_LCSH_General",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_SubdivideGeographically",  # noqa
            ],
        },
        {
            "id": "http://id.loc.gov/authorities/subjects/sh2022001319",
            "label": "Evangelisch Luthersche Kerk (Netherlands)--Relations--Nederlandse Hervormde Kerk",  # noqa
            "deprecated": {
                "status": False,
                "note": "",
                "replacements": [],
                "at": None,
            },
            "collections": [
                "http://id.loc.gov/authorities/subjects/collection_LCSHAuthorizedHeadings",  # noqa
                "http://id.loc.gov/authorities/subjects/collection_LCSH_General",  # noqa
            ],
        },
    ]
