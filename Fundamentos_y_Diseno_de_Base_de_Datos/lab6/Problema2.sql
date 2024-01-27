-- Problema 2
--Determinar la relación de los tres prestatarios rurales más representativos de cada comunidad.
--Los más representativos son los que tienen mayor número de préstamos.
begin
declare @CodComunidad varchar(12);
declare @CodPrestatario varchar(12);
declare @NombrePrestatario varchar(40);
declare @NumPrestamos int;

-- Crear una tabla temporal para almacenar los resultados
create table #Resultados (
    CodComunidad varchar(12),
    CodPrestatario varchar(12),
    NombrePrestatario varchar(40),
    NumPrestamos int
);

-- Declarar cursor para comunidades
declare cursor_Comunidad cursor
for
select CodComunidad from Comunidad;
open cursor_Comunidad;

-- Recorrer comunidades
fetch next from cursor_Comunidad into @CodComunidad;
while @@FETCH_STATUS = 0
begin
    -- Cursor que contará los préstamos de cada prestatario en cada comunidad
    declare cursor_Prestatario cursor
    for
    select P.CodPrestatario, Pr.Nombres, count(*) as NumPrestamos
    from Prestamo P
    join Prestatario Pr on P.CodPrestatario = Pr.CodPrestatario
    where Pr.CodComunidad = @CodComunidad
    group by P.CodPrestatario, Pr.Nombres;

    open cursor_Prestatario;

    -- Recorremos cada uno de los prestatarios para seleccionar los tres con mayor número de préstamos
    declare @Counter int = 0;
    fetch next from cursor_Prestatario into @CodPrestatario, @NombrePrestatario, @NumPrestamos;
    while @@FETCH_STATUS = 0 and @Counter < 3
    begin
        -- Guardamos los resultados obtenidos en la tabla temporal
        insert into #Resultados (CodComunidad, CodPrestatario, NombrePrestatario, NumPrestamos)
        values (@CodComunidad, @CodPrestatario, @NombrePrestatario, @NumPrestamos);

        set @Counter = @Counter + 1;

        -- Siguiente prestatario
        fetch next from cursor_Prestatario into @CodPrestatario, @NombrePrestatario, @NumPrestamos;
    end;

    close cursor_Prestatario;
    deallocate cursor_Prestatario;

    -- Siguiente comunidad
    fetch next from cursor_Comunidad into @CodComunidad;
end;

close cursor_Comunidad;
deallocate cursor_Comunidad;

select * from #Resultados;

-- Eliminar la tabla temporal
drop table #Resultados;
end;
