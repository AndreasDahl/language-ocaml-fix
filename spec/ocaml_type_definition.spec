// SYNTAX TEST "source.ocaml"
type x = int
//<- keyword.other.type-definition.ocaml
//^^^^^^^^^^ meta.type-definition-group.ocaml
//^^^^^^^^^^ !meta.let_binding.ocaml
and y = int
//<- keyword.other.type-definition.ocaml
//^^^^^^^^^ meta.type-definition-group.ocaml
//^^^^^^^^^ !meta.let_binding.ocaml


type x = int

and y = int
//<- keyword.other.type-definition.ocaml
//^^^^^^^^^ meta.type-definition-group.ocaml
//^^^^^^^^^ !meta.let_binding.ocaml


type x = int

(** comment *)
//^^^^^^^^^^^^ comment.block.ocaml
type y = int


type x = int
//^^^^^^^^^^ meta.type-definition-group.ocaml
exception foo
//^^^^^^^^^^^ !meta.type-definition-group.ocaml


type x = int
//^^^^^^^^^^ meta.type-definition-group.ocaml
external y : int -> unit = "y"
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^ !meta.type-definition-group.ocaml


type x = int
//^^^^^^^^^^ meta.type-definition-group.ocaml
module Foo = struct end
//^^^^^^^^^^^^^^^^^^^^^ !meta.type-definition-group.ocaml

type x =
  | Int of int

  | String of string
//^^^^^^^^^^^^^^^^^^ meta.type-definition.ocaml
