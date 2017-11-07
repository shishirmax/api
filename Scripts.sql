--Create Table 
create table formattedAddressData(
		formattedAddress nvarhar(250) NULL,
		latitude nvarhar(250) NULL,
		longitude nvarhar(250) NULL
	)

--Insert into table using SP
create procedure spInsertAddressData
@formattedAddress nvarchar(250),
@latitude nvarchar(250),
@longitude nvarchar(250)
As
Begin
	Insert into formattedAddressData
	values(@formattedAddress,@latitude,@longitude)
End

