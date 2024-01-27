-- Problema 3
-- Determinar los movimientos de un prestatario. Debe mostrar cada préstamo con sus respectivas cancelaciones.
-- Los importes del préstamo van en la columna del Debe y los importes de las
-- cancelaciones van al haber. Considerar que un prestatario puede tener varios préstamos.
begin
declare @CodPrestatario TCodPrestatario;
set @CodPrestatario = 'P01';

-- Crear tabla para almacenar los movimientos de los prestatarios
create table #Movimientos (
    DocMovimiento varchar(12),
    FechaMovimiento datetime,
    Debe numeric(15,2),
    Haber numeric(15,2),
    SaldoPrestado numeric(15,2),
    SaldoTotal numeric(15,2)
);

-- Declarar variables
declare @SaldoPrestado numeric(15,2) = 0;
declare @SaldoTotal numeric(15,2) = 0;

-- Obtener préstamos y cancelaciones del prestatario
insert into #Movimientos
select P.DocPrestamo as DocMovimiento, P.FechaPrestamo as FechaMovimiento, P.Importe as Debe, 0 as Haber, P.Importe as SaldoPrestado,
	   @SaldoTotal + P.Importe as SaldoTotal
from Prestamo P
where P.CodPrestatario = @CodPrestatario
order by P.FechaPrestamo;

insert into #Movimientos
select A.DocCancelacion as DocMovimiento, A.FechaCancelacion as FechaMovimiento, 0 as Debe, A.Importe as Haber, -A.Importe as SaldoPrestado,
       @SaldoTotal - A.Importe as SaldoTotal
from Amortizacion A
where A.DocPrestamo in (select P.DocPrestamo from Prestamo P where P.CodPrestatario = @CodPrestatario)
order by A.FechaCancelacion;

select * from #Movimientos;
drop table #Movimientos;
end;
