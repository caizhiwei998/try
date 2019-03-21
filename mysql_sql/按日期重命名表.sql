set @asql=concat('alter table seo_rankrecords rename `seo_rankrecords',curdate(),'`');
prepare stml from @asql;
EXECUTE stml;
