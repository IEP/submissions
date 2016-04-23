var
  a, b, c : integer;
begin
  a := -2;
  b := a+a;
  c := b*b;
  if a > b then
    if c < b then
      writeln(c)
    else
      writeln(b)
  else
    if c < a then
      writeln(c)
    else
      writeln(a);
end.
