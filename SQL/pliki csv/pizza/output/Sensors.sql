

declare @i int = 1;

while (@i <=101)
	begin
	waitfor delay '00:00:01'
		update sensors set sonsor1 = @i
		update sensors set sonsor2 = rand()*100
	set@i = @i +1;
end
