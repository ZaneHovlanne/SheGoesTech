# 1. get total sales for all years using invoice table
# you will want to use SUBSTR to get the year from the invoice date
# you will want to use SUM to get the total sales for each year
SELECT invoiceid,
    SUBSTRING(invoicedate, 1, 4) as year,
    SUM(Total) as all_sales
FROM invoices
GROUP BY year # 2. get total sales for each country - use invoice table
    # you will also need to join with the customer table - those have country info
SELECT country,
    sum(total) as sales_from_country
FROM invoices i
    Join customers c ON i.customerid = c.customerid
GROUP BY country # 3. a count tracks in each playlist - use playlist_track table
SELECT PlaylistId,
    count(TrackId) as tracks_in_playlist
FROM playlist_track
GROUP BY PlaylistId # 3. b extra challenge get total track lenght in minutes for each playlist
    # you will need to join with the track table
    # 3. c cherry on top - provide names of these playlists
    # so you will want to join with the playlist table as well
SELECT pt.PlaylistId,
    p.Name,
    Count(pt.Trackid) as tracks_in_playlists,
    SUM(t.Milliseconds) /(1000 * 60) as track_length_in_minutes
FROM playlist_track pt
    JOIN tracks t ON pt.TrackId = t.TrackId
    JOIN playlists p ON pt.PlaylistId = p.PlaylistId
GROUP BY pt.PlaylistId