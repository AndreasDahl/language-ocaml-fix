// SYNTAX TEST "source.ocaml"
match x with
| { key = X | Y; } ->
//^^^^^^^^^^^^^^^^ variable.parameter.record.ocaml
//  ^^^ entity.name.tag.record.ocaml
//      ^ punctuation.separator.record.field-assignment.ocaml
//        ^^^^^ meta.recordfield.match.ocaml
//          ^ keyword.operator.match-pattern.ocaml
//             ^ punctuation.separator.record.ocaml
  let foo = ()
//^^^ keyword.other.function-definition.ocaml
//    ^^^ entity.name.function.ocaml

match x with
| { key = X |
//^^^^^^^^^^^ variable.parameter.record.ocaml
//          ^ keyword.operator.match-pattern.ocaml
    Y; } ->
//^^^^^^ variable.parameter.record.ocaml
//   ^ punctuation.separator.record.ocaml
        ^^^ !variable.parameter.record.ocaml
  let foo = ()
//^ !variable.parameter.record.ocaml
//^^^ keyword.other.function-definition.ocaml
//    ^^^ entity.name.function.ocaml

begin match x with
  (* | comment *)
//^^^^^^^^^^^^^^^ comment.block.ocaml
| A -> ()
end
