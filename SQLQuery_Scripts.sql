SELECT  [Address],Latitude,Longitude FROM tblSales_24102017
FOR JSON PATH 

CREATE TABLE googleApiAddress(
	ID INT IDENTITY(1,1),
	FormattedAddress VARCHAR(250) NULL,
	Latitude VARCHAR(250) NULL,
	Longitude VARCHAR(250) NULL)

select * from googleApiAddress

select count(*) from tblSales_24102017
where RecordIDs = '1037616'

select * from edina_google_normalized

select max(LEN([formatted address])) from edina_google_normalized

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


CREATE TABLE[dbo].[Tweets_JSON]  
    (  
        [JSON_STRING][varchar](max) NULL)  
BULK INSERT[dbo].[Tweets_JSON]  FROM 'D:\GIT\api\curl_data\newdelhi.txt'

select * from [Tweets_JSON]

SELECT J.*FROM[dbo].[Tweets_JSON]  
CROSS APPLY OPENJSON(JSON_STRING)  
With(  
    [results] Varchar(100)
)J