"""MSGraph tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_ms_graph.streams import UsersStream

STREAM_TYPES = [
    UsersStream,
]


class TapMSGraph(Tap):
    """MSGraph tap class."""

    name = "tap-ms-graph"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "tenant",
            th.StringType,
            required=True,
            description="The directory tenant to request permission from. The value can be in GUID or a friendly name format.",
        ),
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="The application ID that the Azure app registration portal assigned to the registered app.",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="The client secret generated for the app in the app registration portal.",
        ),
        #        th.Property(
        #            'start_date',
        #            th.DateTimeType,
        #            description='The earliest record date to sync'
        #        ),
        th.Property(
            "stream_config",
            th.ArrayType(
                th.PropertiesList(
                    th.Property(
                        "stream",
                        th.StringType,
                        description="Name of stream to apply a custom configuration.",
                    ),
                    th.Property(
                        "params",
                        th.PropertiesList(
                            th.Property(
                                "$count",
                                th.BooleanType,
                                description="Retrieves the total count of matching resources.",
                            ),
                            th.Property(
                                "$expand",
                                th.StringType,
                                description="Retrieves related resources.",
                            ),
                            th.Property(
                                "$filter",
                                th.StringType,
                                description="Filters results (rows).",
                            ),
                            th.Property(
                                "$orderby",
                                th.ArrayType(th.StringType),
                                description="Orders results.",
                            ),
                            th.Property(
                                "$search",
                                th.StringType,
                                description="Returns results based on search criteria.",
                            ),
                            th.Property(
                                "$select",
                                th.ArrayType(th.StringType),
                                description="Filters properties (columns).",
                            ),
                            th.Property(
                                "$skip",
                                th.IntegerType,
                                description="Indexes into a result set.",
                            ),
                            th.Property(
                                "$top",
                                th.IntegerType,
                                description="Sets the page size of results.",
                            ),
                        ),
                    ),
                )
            ),
            description="Custom configuration for streams.",
        ),
        th.Property(
            "api_version",
            th.StringType,
            default="v1.0",
            # allowed_values=['v1.0', 'beta'],
            allowed_values=["v1.0"],
            description="The version of the Microsoft Graph API to use.",
        ),
        th.Property(
            "auth_url",
            th.StringType,
            description="Override the Azure AD authentication base URL. Required if using a national cloud.",
        ),
        th.Property(
            "api_url",
            th.StringType,
            description="Override the Graph API service base URL. Required if using a national cloud.",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapMSGraph.cli()
