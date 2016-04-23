var
  b1, b2, jml: longint;
begin
  b1 := 2000000000;
  b2 := 2000000000;

  jml := (b1+b2) mod 123;
  writeln(jml);
end.
