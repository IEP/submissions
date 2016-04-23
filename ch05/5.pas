var
  a : integer;
begin
  a := 26;
  if not (a and 1 = 0) then
    write('genap ')
  else
    write('ganjil ');

  if (a > 0) then
    writeln('positif')
  else if (a < 0) then
    writeln('negatif')
  else
    writeln('nol');
end.
