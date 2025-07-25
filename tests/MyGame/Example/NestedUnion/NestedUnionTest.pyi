from __future__ import annotations

import flatbuffers
import numpy as np

import typing
from MyGame.Example.NestedUnion.Any import Any
from MyGame.Example.NestedUnion.TestSimpleTableWithEnum import TestSimpleTableWithEnumT
from MyGame.Example.NestedUnion.Vec3 import Vec3T
from flatbuffers import table

uoffset: typing.TypeAlias = flatbuffers.number_types.UOffsetTFlags.py_type

class NestedUnionTest(object):
  @classmethod
  def GetRootAs(cls, buf: bytes, offset: int) -> NestedUnionTest: ...
  @classmethod
  def GetRootAsNestedUnionTest(cls, buf: bytes, offset: int) -> NestedUnionTest: ...
  def Init(self, buf: bytes, pos: int) -> None: ...
  def Name(self) -> str | None: ...
  def DataType(self) -> typing.Literal[Any.NONE, Any.Vec3, Any.TestSimpleTableWithEnum]: ...
  def Data(self) -> table.Table | None: ...
  def Id(self) -> int: ...
class NestedUnionTestT(object):
  name: str | None
  dataType: typing.Literal[Any.NONE, Any.Vec3, Any.TestSimpleTableWithEnum]
  data: typing.Union[None, Vec3T, TestSimpleTableWithEnumT]
  id: int
  def __init__(
    self,
    name: str | None = ...,
    dataType: typing.Literal[Any.NONE, Any.Vec3, Any.TestSimpleTableWithEnum] = ...,
    data: typing.Union[None, Vec3T, TestSimpleTableWithEnumT] = ...,
    id: int = ...,
  ) -> None: ...
  @classmethod
  def InitFromBuf(cls, buf: bytes, pos: int) -> NestedUnionTestT: ...
  @classmethod
  def InitFromPackedBuf(cls, buf: bytes, pos: int = 0) -> NestedUnionTestT: ...
  @classmethod
  def InitFromObj(cls, nestedUnionTest: NestedUnionTest) -> NestedUnionTestT: ...
  def _UnPack(self, nestedUnionTest: NestedUnionTest) -> None: ...
  def Pack(self, builder: flatbuffers.Builder) -> None: ...
def NestedUnionTestStart(builder: flatbuffers.Builder) -> None: ...
def Start(builder: flatbuffers.Builder) -> None: ...
def NestedUnionTestAddName(builder: flatbuffers.Builder, name: uoffset) -> None: ...
def NestedUnionTestAddDataType(builder: flatbuffers.Builder, dataType: typing.Literal[Any.NONE, Any.Vec3, Any.TestSimpleTableWithEnum]) -> None: ...
def NestedUnionTestAddData(builder: flatbuffers.Builder, data: uoffset) -> None: ...
def NestedUnionTestAddId(builder: flatbuffers.Builder, id: int) -> None: ...
def NestedUnionTestEnd(builder: flatbuffers.Builder) -> uoffset: ...
def End(builder: flatbuffers.Builder) -> uoffset: ...

