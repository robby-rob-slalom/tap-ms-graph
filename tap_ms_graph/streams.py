"""Stream type classes for tap-ms-graph."""
from __future__ import annotations

from tap_ms_graph.client import MSGraphChildStream, MSGraphStream


class GroupsStream(MSGraphStream):
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    odata_context = "groups"
    child_context = {"id": "group_id"}


class GroupMembersStream(MSGraphChildStream):
    parent_stream_type = GroupsStream
    name = "groupMembers"
    path = "/groups/{group_id}/members"
    primary_keys = ["group_id", "id"]
    odata_context = "directoryObjects"
    odata_type = "microsoft.graph.user"
    state_partitioning_keys = []

    # TODO: find a way to make this automatic
    parent_context_schema = {
        "group_id": {"type": "string"},
    }
class GroupOwnersStream(MSGraphChildStream):
    parent_stream_type = GroupsStream
    name = "groupOwners"
    path = "/groups/{group_id}/owners?$top=1"
    primary_keys = ["group_id", "id"]
    odata_context = "directoryObjects"
    odata_type = "microsoft.graph.user"

    # TODO: find a way to make this automatic
    parent_context_schema = {
        "group_id": {"type": "string"},
    }
class GroupMetadataStream(MSGraphChildStream):
    parent_stream_type = GroupsStream
    name = "groupMetadata"
    path = "/groups/{group_id}"
    primary_keys = ["group_id","id"]
    odata_context = "groups"
    odata_type = "microsoft.graph.groups"
    parent_context_schema = {
        "group_id": {"type": "string"},
    }

class SubscribedSkusStream(MSGraphStream):
    name = "subscribedSkus"
    path = "/subscribedSkus"
    primary_keys = ["id"]
    odata_context = "subscribedSkus"


class UsersStream(MSGraphStream):
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    odata_context = "users"
