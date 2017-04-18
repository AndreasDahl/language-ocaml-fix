// SYNTAX TEST "source.ocaml"
(* test *)
// ^^^^ comment.block.ocaml
fun x -> y
// <- keyword.other.function-definition.ocaml
// <- meta.function.anonymous.definition.ocaml
//^^^^^^ meta.function.anonymous.definition.ocaml
//  ^ variable.parameter.ocaml
//    ^^ keyword.other.anonymous-function-arrow.ocaml
//      ^^ !meta.function.anonymous.definition.ocaml
begin fun x -> y end
// <- keyword.control.begin-end.ocaml
//    ^^^^^^^^ meta.function.anonymous.definition.ocaml
//    ^^^ meta.function.anonymous.definition.ocaml
//        ^ variable.parameter.ocaml
//          ^^ keyword.other.anonymous-function-arrow.ocaml
//             ^^^^^ !meta.function.anonymous.definition.ocaml
//               ^^^ keyword.control.begin-end.ocaml
   a>>=b
//  ^^^ entity.name.function.infix.ocaml
   a->b
//  ^^ punctuation.separator.function-return.ocaml
   a->>b
//  ^^^ entity.name.function.infix.ocaml
   a+.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a-.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a/.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a*.b
//  ^^ keyword.operator.infix.floating-point.ocaml
   a+b
//  ^ keyword.operator.infix.integer.ocaml
   a-b
//  ^ keyword.operator.infix.integer.ocaml
   a/b
//  ^ keyword.operator.infix.integer.ocaml
   a*b
//  ^ keyword.operator.infix.integer.ocaml
val test: a -> b
// <- keyword.other.ocaml
//  ^^^^ entity.name.type.value-signature.ocaml
//      ^ punctuation.separator.type-constraint.ocaml
//        ^ storage.type.ocaml
//          ^^ punctuation.separator.function-return.ocaml
//             ^ storage.type.ocaml
val ( >> ): a -> b
// <- keyword.other.ocaml
//  ^^^^^^ entity.name.type.value-signature.ocaml
//        ^ punctuation.separator.type-constraint.ocaml
//          ^ storage.type.ocaml
//            ^^ punctuation.separator.function-return.ocaml
//               ^ storage.type.ocaml
fun () -> a
// <- keyword.other.function-definition.ocaml
// <- meta.function.anonymous.definition.ocaml
//^^^^^^^ meta.function.anonymous.definition.ocaml
//  ^^ constant.language.unit.ocaml
//     ^^ keyword.other.anonymous-function-arrow.ocaml
fun _ -> a
// <- keyword.other.function-definition.ocaml
// <- meta.function.anonymous.definition.ocaml
//^^^^^^ meta.function.anonymous.definition.ocaml
//  ^ constant.language.universal-match.ocaml
//    ^^ keyword.other.anonymous-function-arrow.ocaml
begin function
  | a
//^ keyword.control.match-definition.ocaml
  | a -> a
//^ keyword.control.match-definition.ocaml
//    ^^ punctuation.separator.match-definition.ocaml
end
begin match a with
  | b
//^ keyword.control.match-definition.ocaml
  | b -> b
//^ keyword.control.match-definition.ocaml
//    ^^ punctuation.separator.match-definition.ocaml
end
begin
  raise a
//^^^^^ support.function
  raise_notrace a
//^^^^^^^^^^^^^ support.function
  invalid_arg a
//^^^^^^^^^^^ support.function
  failwith a
//^^^^^^^^ support.function
  compare a b
//^^^^^^^ support.function
  min a b
//^^^ support.function
  max a b
//^^^ support.function
 a=b
//^ support.function
 a<>b
//^^ support.function
 a<b
//^ support.function
 a>b
//^ support.function
 a<=b
//^^ support.function
 a>=b
//^^ support.function
 a==b
//^^ support.function
 a!=b
//^^ support.function
  not a
//^^^ support.function
a or b
//^^ invalid.deprecated
 a&&b
//^^ support.function
  a&b
// ^ invalid.deprecated
 a||b
//^^ support.function
 a|>b
//^^ support.function
 a@@b
//^^ support.function
 a^b
//^ support.function
end

  (*  *)
//^^^^^^ comment.block.ocaml
  (* "test" *)
//^^^^^^^^^^^^ comment.block.ocaml
  (* "*)" *)
//^^^^^^^^^^ comment.block.ocaml
