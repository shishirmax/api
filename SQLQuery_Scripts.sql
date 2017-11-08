SELECT  [Address],Latitude,Longitude FROM tblSales_24102017
FOR JSON PATH 

CREATE TABLE googleApiAddress(
	ID INT IDENTITY(1,1),
	FormattedAddress VARCHAR(250) NULL,
	Latitude VARCHAR(250) NULL,
	Longitude VARCHAR(250) NULL)

select * from googleApiAddress

select count(*) from tblSales_24102017


CREATE PROCEDURE spInsertAddressData
@formattedAddress NVARCHAR(250),
@latitude NVARCHAR(250),
@longitude NVARCHAR(250)
AS
BEGIN
	INSERT INTO googleApiAddress
	VALUES(@formattedAddress,@latitude,@longitude)
END



declare @PageNumber int = 3
	SELECT * FROM (SELECT    ROW_NUMBER() OVER(ORDER BY SALESID) AS Number,[address],Latitude,Longitude
			FROM tblsales_24102017) AS TBL
WHERE Number BETWEEN ((@PageNumber - 1) * 500 + 1) AND (@PageNumber * 500)
ORDER BY Number