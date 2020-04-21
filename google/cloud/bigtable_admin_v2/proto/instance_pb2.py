# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigtable/admin_v2/proto/instance.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.bigtable_admin_v2.proto import (
    common_pb2 as google_dot_cloud_dot_bigtable_dot_admin__v2_dot_proto_dot_common__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigtable/admin_v2/proto/instance.proto",
    package="google.bigtable.admin.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.bigtable.admin.v2B\rInstanceProtoP\001Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\252\002\036Google.Cloud.Bigtable.Admin.V2\312\002\036Google\\Cloud\\Bigtable\\Admin\\V2"
    ),
    serialized_pb=_b(
        '\n3google/cloud/bigtable/admin_v2/proto/instance.proto\x12\x18google.bigtable.admin.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x31google/cloud/bigtable/admin_v2/proto/common.proto"\xdd\x03\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12\x19\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x37\n\x05state\x18\x03 \x01(\x0e\x32(.google.bigtable.admin.v2.Instance.State\x12\x35\n\x04type\x18\x04 \x01(\x0e\x32\'.google.bigtable.admin.v2.Instance.Type\x12>\n\x06labels\x18\x05 \x03(\x0b\x32..google.bigtable.admin.v2.Instance.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"5\n\x05State\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08\x43REATING\x10\x02"=\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\x0f\n\x0b\x44\x45VELOPMENT\x10\x02:N\xea\x41K\n bigtable.googleapis.com/Instance\x12\'projects/{project}/instances/{instance}"\xa7\x03\n\x07\x43luster\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x03\x12\x38\n\x08location\x18\x02 \x01(\tB&\xfa\x41#\n!locations.googleapis.com/Location\x12;\n\x05state\x18\x03 \x01(\x0e\x32\'.google.bigtable.admin.v2.Cluster.StateB\x03\xe0\x41\x03\x12\x18\n\x0bserve_nodes\x18\x04 \x01(\x05\x42\x03\xe0\x41\x02\x12\x43\n\x14\x64\x65\x66\x61ult_storage_type\x18\x05 \x01(\x0e\x32%.google.bigtable.admin.v2.StorageType"Q\n\x05State\x12\x13\n\x0fSTATE_NOT_KNOWN\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08\x43REATING\x10\x02\x12\x0c\n\x08RESIZING\x10\x03\x12\x0c\n\x08\x44ISABLED\x10\x04:`\xea\x41]\n\x1f\x62igtable.googleapis.com/Cluster\x12:projects/{project}/instances/{instance}/clusters/{cluster}"\xee\x03\n\nAppProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12g\n\x1dmulti_cluster_routing_use_any\x18\x05 \x01(\x0b\x32>.google.bigtable.admin.v2.AppProfile.MultiClusterRoutingUseAnyH\x00\x12[\n\x16single_cluster_routing\x18\x06 \x01(\x0b\x32\x39.google.bigtable.admin.v2.AppProfile.SingleClusterRoutingH\x00\x1a\x1b\n\x19MultiClusterRoutingUseAny\x1aN\n\x14SingleClusterRouting\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12"\n\x1a\x61llow_transactional_writes\x18\x02 \x01(\x08:j\xea\x41g\n"bigtable.googleapis.com/AppProfile\x12\x41projects/{project}/instances/{instance}/appProfiles/{app_profile}B\x10\n\x0erouting_policyB\xb0\x01\n\x1c\x63om.google.bigtable.admin.v2B\rInstanceProtoP\x01Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_bigtable_dot_admin__v2_dot_proto_dot_common__pb2.DESCRIPTOR,
    ],
)


_INSTANCE_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.bigtable.admin.v2.Instance.State",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_NOT_KNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="READY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CREATING", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=474,
    serialized_end=527,
)
_sym_db.RegisterEnumDescriptor(_INSTANCE_STATE)

_INSTANCE_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="google.bigtable.admin.v2.Instance.Type",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PRODUCTION", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DEVELOPMENT", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=529,
    serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_INSTANCE_TYPE)

_CLUSTER_STATE = _descriptor.EnumDescriptor(
    name="State",
    full_name="google.bigtable.admin.v2.Cluster.State",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STATE_NOT_KNOWN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="READY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CREATING", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="RESIZING", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DISABLED", index=4, number=4, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=917,
    serialized_end=998,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_STATE)


_INSTANCE_LABELSENTRY = _descriptor.Descriptor(
    name="LabelsEntry",
    full_name="google.bigtable.admin.v2.Instance.LabelsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.bigtable.admin.v2.Instance.LabelsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.bigtable.admin.v2.Instance.LabelsEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=427,
    serialized_end=472,
)

_INSTANCE = _descriptor.Descriptor(
    name="Instance",
    full_name="google.bigtable.admin.v2.Instance",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.bigtable.admin.v2.Instance.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\003"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.bigtable.admin.v2.Instance.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.bigtable.admin.v2.Instance.state",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.bigtable.admin.v2.Instance.type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="labels",
            full_name="google.bigtable.admin.v2.Instance.labels",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_INSTANCE_LABELSENTRY,],
    enum_types=[_INSTANCE_STATE, _INSTANCE_TYPE,],
    serialized_options=_b(
        "\352AK\n bigtable.googleapis.com/Instance\022'projects/{project}/instances/{instance}"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=193,
    serialized_end=670,
)


_CLUSTER = _descriptor.Descriptor(
    name="Cluster",
    full_name="google.bigtable.admin.v2.Cluster",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.bigtable.admin.v2.Cluster.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\003"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="location",
            full_name="google.bigtable.admin.v2.Cluster.location",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\372A#\n!locations.googleapis.com/Location"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="state",
            full_name="google.bigtable.admin.v2.Cluster.state",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\003"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="serve_nodes",
            full_name="google.bigtable.admin.v2.Cluster.serve_nodes",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="default_storage_type",
            full_name="google.bigtable.admin.v2.Cluster.default_storage_type",
            index=4,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_CLUSTER_STATE,],
    serialized_options=_b(
        "\352A]\n\037bigtable.googleapis.com/Cluster\022:projects/{project}/instances/{instance}/clusters/{cluster}"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=673,
    serialized_end=1096,
)


_APPPROFILE_MULTICLUSTERROUTINGUSEANY = _descriptor.Descriptor(
    name="MultiClusterRoutingUseAny",
    full_name="google.bigtable.admin.v2.AppProfile.MultiClusterRoutingUseAny",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1360,
    serialized_end=1387,
)

_APPPROFILE_SINGLECLUSTERROUTING = _descriptor.Descriptor(
    name="SingleClusterRouting",
    full_name="google.bigtable.admin.v2.AppProfile.SingleClusterRouting",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="cluster_id",
            full_name="google.bigtable.admin.v2.AppProfile.SingleClusterRouting.cluster_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="allow_transactional_writes",
            full_name="google.bigtable.admin.v2.AppProfile.SingleClusterRouting.allow_transactional_writes",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1389,
    serialized_end=1467,
)

_APPPROFILE = _descriptor.Descriptor(
    name="AppProfile",
    full_name="google.bigtable.admin.v2.AppProfile",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.bigtable.admin.v2.AppProfile.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.bigtable.admin.v2.AppProfile.etag",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.bigtable.admin.v2.AppProfile.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="multi_cluster_routing_use_any",
            full_name="google.bigtable.admin.v2.AppProfile.multi_cluster_routing_use_any",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="single_cluster_routing",
            full_name="google.bigtable.admin.v2.AppProfile.single_cluster_routing",
            index=4,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _APPPROFILE_MULTICLUSTERROUTINGUSEANY,
        _APPPROFILE_SINGLECLUSTERROUTING,
    ],
    enum_types=[],
    serialized_options=_b(
        '\352Ag\n"bigtable.googleapis.com/AppProfile\022Aprojects/{project}/instances/{instance}/appProfiles/{app_profile}'
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="routing_policy",
            full_name="google.bigtable.admin.v2.AppProfile.routing_policy",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=1099,
    serialized_end=1593,
)

_INSTANCE_LABELSENTRY.containing_type = _INSTANCE
_INSTANCE.fields_by_name["state"].enum_type = _INSTANCE_STATE
_INSTANCE.fields_by_name["type"].enum_type = _INSTANCE_TYPE
_INSTANCE.fields_by_name["labels"].message_type = _INSTANCE_LABELSENTRY
_INSTANCE_STATE.containing_type = _INSTANCE
_INSTANCE_TYPE.containing_type = _INSTANCE
_CLUSTER.fields_by_name["state"].enum_type = _CLUSTER_STATE
_CLUSTER.fields_by_name[
    "default_storage_type"
].enum_type = (
    google_dot_cloud_dot_bigtable_dot_admin__v2_dot_proto_dot_common__pb2._STORAGETYPE
)
_CLUSTER_STATE.containing_type = _CLUSTER
_APPPROFILE_MULTICLUSTERROUTINGUSEANY.containing_type = _APPPROFILE
_APPPROFILE_SINGLECLUSTERROUTING.containing_type = _APPPROFILE
_APPPROFILE.fields_by_name[
    "multi_cluster_routing_use_any"
].message_type = _APPPROFILE_MULTICLUSTERROUTINGUSEANY
_APPPROFILE.fields_by_name[
    "single_cluster_routing"
].message_type = _APPPROFILE_SINGLECLUSTERROUTING
_APPPROFILE.oneofs_by_name["routing_policy"].fields.append(
    _APPPROFILE.fields_by_name["multi_cluster_routing_use_any"]
)
_APPPROFILE.fields_by_name[
    "multi_cluster_routing_use_any"
].containing_oneof = _APPPROFILE.oneofs_by_name["routing_policy"]
_APPPROFILE.oneofs_by_name["routing_policy"].fields.append(
    _APPPROFILE.fields_by_name["single_cluster_routing"]
)
_APPPROFILE.fields_by_name[
    "single_cluster_routing"
].containing_oneof = _APPPROFILE.oneofs_by_name["routing_policy"]
DESCRIPTOR.message_types_by_name["Instance"] = _INSTANCE
DESCRIPTOR.message_types_by_name["Cluster"] = _CLUSTER
DESCRIPTOR.message_types_by_name["AppProfile"] = _APPPROFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Instance = _reflection.GeneratedProtocolMessageType(
    "Instance",
    (_message.Message,),
    dict(
        LabelsEntry=_reflection.GeneratedProtocolMessageType(
            "LabelsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_INSTANCE_LABELSENTRY,
                __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2"
                # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Instance.LabelsEntry)
            ),
        ),
        DESCRIPTOR=_INSTANCE,
        __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2",
        __doc__="""A collection of Bigtable [Tables][google.bigtable.admin.v2.Table] and
  the resources that serve them. All tables in an instance are served
  from all [Clusters][google.bigtable.admin.v2.Cluster] in the instance.
  Attributes:
      name:
          The unique name of the instance. Values are of the form
          ``projects/{project}/instances/[a-z][a-z0-9\\-]+[a-z0-9]``.
      display_name:
          Required. The descriptive name for this instance as it appears
          in UIs. Can be changed at any time, but should be kept
          globally unique to avoid confusion.
      state:
          (\ ``OutputOnly``) The current state of the instance.
      type:
          The type of the instance. Defaults to ``PRODUCTION``.
      labels:
          Labels are a flexible and lightweight mechanism for organizing
          cloud resources into groups that reflect a customer's
          organizational needs and deployment strategies. They can be
          used to filter resources and aggregate metrics.  -  Label keys
          must be between 1 and 63 characters long and must conform
          to the regular expression:
          ``[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}``. -  Label values
          must be between 0 and 63 characters long and must    conform
          to the regular expression: ``[\p{Ll}\p{Lo}\p{N}_-]{0,63}``. -
          No more than 64 labels can be associated with a given
          resource. -  Keys and values must both be under 128 bytes.
  """,
        # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Instance)
    ),
)
_sym_db.RegisterMessage(Instance)
_sym_db.RegisterMessage(Instance.LabelsEntry)

Cluster = _reflection.GeneratedProtocolMessageType(
    "Cluster",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CLUSTER,
        __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2",
        __doc__="""A resizable group of nodes in a particular cloud location, capable of
  serving all [Tables][google.bigtable.admin.v2.Table] in the parent
  [Instance][google.bigtable.admin.v2.Instance].
  Attributes:
      name:
          The unique name of the cluster. Values are of the form ``proje
          cts/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*``.
      location:
          (\ ``CreationOnly``) The location where this cluster's nodes
          and storage reside. For best performance, clients should be
          located as close as possible to this cluster. Currently only
          zones are supported, so values should be of the form
          ``projects/{project}/locations/{zone}``.
      state:
          The current state of the cluster.
      serve_nodes:
          Required. The number of nodes allocated to this cluster. More
          nodes enable higher throughput and more consistent
          performance.
      default_storage_type:
          (\ ``CreationOnly``) The type of storage used by this cluster
          to serve its parent instance's tables, unless explicitly
          overridden.
  """,
        # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.Cluster)
    ),
)
_sym_db.RegisterMessage(Cluster)

AppProfile = _reflection.GeneratedProtocolMessageType(
    "AppProfile",
    (_message.Message,),
    dict(
        MultiClusterRoutingUseAny=_reflection.GeneratedProtocolMessageType(
            "MultiClusterRoutingUseAny",
            (_message.Message,),
            dict(
                DESCRIPTOR=_APPPROFILE_MULTICLUSTERROUTINGUSEANY,
                __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2",
                __doc__="""Read/write requests are routed to the nearest cluster in the instance,
    and will fail over to the nearest cluster that is available in the
    event of transient errors or delays. Clusters in a region are
    considered equidistant. Choosing this option sacrifices read-your-
    writes consistency to improve availability.""",
                # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.AppProfile.MultiClusterRoutingUseAny)
            ),
        ),
        SingleClusterRouting=_reflection.GeneratedProtocolMessageType(
            "SingleClusterRouting",
            (_message.Message,),
            dict(
                DESCRIPTOR=_APPPROFILE_SINGLECLUSTERROUTING,
                __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2",
                __doc__="""Unconditionally routes all read/write requests to a specific cluster.
    This option preserves read-your-writes consistency but does not
    improve availability.
    Attributes:
        cluster_id:
            The cluster to which read/write requests should be routed.
        allow_transactional_writes:
            Whether or not ``CheckAndMutateRow`` and
            ``ReadModifyWriteRow`` requests are allowed by this app
            profile. It is unsafe to send these requests to the same
            table/row/column in multiple clusters.
    """,
                # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.AppProfile.SingleClusterRouting)
            ),
        ),
        DESCRIPTOR=_APPPROFILE,
        __module__="google.cloud.bigtable.admin_v2.proto.instance_pb2",
        __doc__="""A configuration object describing how Cloud Bigtable should treat
  traffic from a particular end user application.
  Attributes:
      name:
          (\ ``OutputOnly``) The unique name of the app profile. Values
          are of the form
          ``projects/<project>/instances/<instance>/appProfiles/[_a-
          zA-Z0-9][-_.a-zA-Z0-9]*``.
      etag:
          Strongly validated etag for optimistic concurrency control.
          Preserve the value returned from ``GetAppProfile`` when
          calling ``UpdateAppProfile`` to fail the request if there has
          been a modification in the mean time. The ``update_mask`` of
          the request need not include ``etag`` for this protection to
          apply. See `Wikipedia
          <https://en.wikipedia.org/wiki/HTTP_ETag>`__ and `RFC 7232
          <https://tools.ietf.org/html/rfc7232#section-2.3>`__ for more
          details.
      description:
          Optional long form description of the use case for this
          AppProfile.
      routing_policy:
          The routing policy for all read/write requests that use this
          app profile. A value must be explicitly set.
      multi_cluster_routing_use_any:
          Use a multi-cluster routing policy.
      single_cluster_routing:
          Use a single-cluster routing policy.
  """,
        # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.AppProfile)
    ),
)
_sym_db.RegisterMessage(AppProfile)
_sym_db.RegisterMessage(AppProfile.MultiClusterRoutingUseAny)
_sym_db.RegisterMessage(AppProfile.SingleClusterRouting)


DESCRIPTOR._options = None
_INSTANCE_LABELSENTRY._options = None
_INSTANCE.fields_by_name["name"]._options = None
_INSTANCE.fields_by_name["display_name"]._options = None
_INSTANCE._options = None
_CLUSTER.fields_by_name["name"]._options = None
_CLUSTER.fields_by_name["location"]._options = None
_CLUSTER.fields_by_name["state"]._options = None
_CLUSTER.fields_by_name["serve_nodes"]._options = None
_CLUSTER._options = None
_APPPROFILE._options = None
# @@protoc_insertion_point(module_scope)
