(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('新蔡县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"411729","properties":{"name":"新蔡县","cp":[114.96547,32.744896],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@A@@@@@AA@A@@B@@A@AA@@@A@@@AA@AKFACCB@AAA@@A@@@AEE@@A@A@A@@@ABAB@@A@@@@@CB@@@@@B@@@@BJA@@A@@@D@@@DA@@BA@@BD@@BA@@BB@@@A@B@@B@@BB@@@AB@@@@@BB@B@@A@BDB@@@@@BBC@@BB@@DA@@BA@@B@@A@A@@@EB@@@@A@EBA@ABCB@@A@@@A@A@A@@@A@@BA@AA@@@@A@@A@A@@@@AAA@AAA@@@@BIB@BEBB@A@BDABBBA@@@A@@BC@BDC@@@ABB@CBAAAB@@@J@B@@@@BB@BB@AB@F@B@BAB@B@@ABAB@BA@@BAB@BA@AAA@@@@@@BC@C@C@A@@@A@@A@AA@C@A@@@@@@A@@@@@ABA@@A@@@A@CBA@@AE@C@A@CCBA@AA@AA@@AC@@EBA@@@@@A@CBCDA@CDA@@BEFCDA@AB@@@DCB@BEBB@EB@BC@@BA@@B@@A@@CC@@B@AC@BD@BC@ABC@ACC@IBA@CHA@@@A@@BA@@@A@CB@B@@C@@@A@A@AAGB@@AC@@A@GDMFA@ABA@G@MBM@@@E@SBA@IEUIEA@A@AA@@AA@@@@@C@@BCA@AAAA@@@@A@@@@A@@AC@@@@@A@AAC@@DA@@AA@@BC@@DAAA@@DE@@DA@@DU@@@AB@@A@A@@CC@AB@@@@@A@@@@@@@@A@@C@@@@AB@@ABCB@BAB@@A@@B@@B@@B@@@@@@A@@@C@@@@@A@AB@@@@BB@@@@@@@@AB@@@@A@A@@@@@@B@@DB@@B@@BA@@@A@@@@B@@@B@@AAA@@BB@BB@B@@@@ABABA@A@C@I@E@G@A@A@@BA@@BAD@BAD@@@@A@@@CEA@@@A@@@@@AH@@C@@@C@A@GCAA@@AA@@@A@ADABA@@@AA@AACCAAA@AA@@@A@@BE@A@@@ACAEA@A@A@@@A@@B@D@D@BAB@BA@A@@@AAAAA@@ECGCCAAAA@@@A@@BA@@B@BABBF@B@BA@@BABABC@ABA@@A@@@A@ABA@CBA@A@C@@AA@A@@A@KC@@A@@@A@@DAB@@@@A@@@AAACA@@@EAAAC@I@C@GAEAA@C@A@ABA@A@@BAB@@@B@@@BB@@BB@F@D@B@@@BBB@@B@@@BABA@ADAB@BA@CAEACAC@CAA@A@AAECCAAAA@A@A@C@A@ABA@A@@B@DABABABABA@@BA@A@E@KAC@C@AB@@AB@@BBBFBB@@@B@B@@A@@BA@AACAAACCAAA@AAA@A@EBABA@AB@@B@@BFBBBBBFFDF@B@BCBA@@BAAA@ACAAC@AAAACAACAAA@CAC@A@@BA@@@@BBF@D@BBB@BDDBB@@@BAB@B@BB@@@@BD@BAB@BBB@DB@@DDFD@@BB@@@BA@@BABA@A@C@C@A@ABCFAD@@CBABA@A@A@A@@AA@@A@@BABAB@@ABA@A@A@@AAC@@@A@AAEGA@@AC@C@A@AAC@@ACC@AAAAA@@AAA@ABA@A@AB@B@B@BBB@@BB@@D@D@B@B@BB@@BB@@@B@BCFA@ADA@A@A@@@@AAA@A@CA@@AA@CCA@CAC@C@ABKDCBABA@AB@@@BDB@B@@@B@@@BA@A@C@A@ABA@@DABAB@@A@A@CAC@C@C@C@A@A@ABAFABABCDA@@B@B@@BDBB@B@BA@@@ED@@ABADADABADA@@B@B@@@B@@B@B@BAB@B@BB@@@B@@CDAB@@@DA@@B@B@BB@@@B@D@@B@@@@@B@@ABAB@B@@BBBB@@B@@@BB@@BAD@B@@B@@C@@@@BF@@@@DD@@@B@@BB@B@@D@@A@@@B@AB@@IDBF@@@@@F@@@@D@@@BF@@B@@@B@BA@B@D@B@@@D@@@@@@A@@BABABBNH@@@BB@BHCBAD@@A@B@BBF@@@@@@BF@@B@@B@BB@BDD@@BB@@BBB@@@C@@B@@F@@B@@BDA@AP@BB@@B@BB@@ABDHBDA@BF@@@@@B@@EB@A@@C@@@BDMB@B@@A@@@A@@@DHLA@@@BF@AA@@FA@@AAB@@B@@B@AAB@@BB@@A@@DA@B@EHAAAD@@@B@@AB@@@@A@@B@@@@@BFA@BF@@A@BBA@@DBJB@@B@@@D@@@@@@@@AB@AA@@@@@CB@AC@@@@BABBBGB@B@@@BAB@CA@BL@BXEBD@A@BBFB@@JA@@B@@@@F@BFD@@DBF@@@DA@@BA@@DC@@F@@@DB@@BB@BHBPB@@D@@@D@F@B@D@@@B@@@B@BB@@B@@@@@BBB@@B@@@DD@@DABBB@BBB@@@B@@@@AB@HAHCFAFAB@BADAB@DAB@B@BBB@HDB@DDB@@BHFBBHHDBBBDBBBFBLF@@@@@@AD@D@@AH@F@B@B@D@B@BB@BF@B@@@BAF@B@@@@DFBB@B@B@@B@P@@CRAJ@@@BD@BD@@B@BH@@AF@PA@FDA@BB@@BA@BD@BBD@@@BDHBF@@@@BBB@B@@@DABHB@@@B@B@@B@@BD@DB@@B@@H@@B@@J@@@@@J@@@@BF@@A@C@@@@BA@AD@@@J@LB@@@HA@@BB@@FGAADI@@@@@@@A@CA@@@HAB@B@BH@@BF@@@@@@D@@H@@BFB@DF@@B@B@@@DDB@ABAB@@BFB@A@AFBB@@B@BJJDCHAJCL@N@F@B@B@BCDGBCDEDCB@DAHADC@@FCHSDIDEDAF@F@JFBBFD@@D@H@NBL@NBDAH@L@J@NALE@@HAVIFABABC@ADCBABC@C@AAAAA@@OC@@A@AAAAAA@A@ABABAFATAN@F@HALAB@F@@@HAB@NBP@D@B@BADAHEFEFADAB@@@B@FBBBHDHDD@F@H@JAJ@HAF@B@DCBABA@AACAE@A@C@ADADCJAB@DCBA@@BEAG@GBA@AHELCBAF@NEH@B@HBLBBAF@DADCDGBGBE@ACAKBIA@@AAAEBEBADCDCDA@@@CACEGCK@C@EBABAFGBABAHCLEDC@AHI@@@A@AACC@E@I@GBGDEDA@A@A@EACAAA@A@AAG@@BE@@B@@CFABCDABC@E@EAAACCMAACMAICAAA@A@GAG@@BE@EBADABABA@C@A@CAICE@AACAC@E@ABEDCBA@AAC@EAAAAACA@@A@A@@DAD@B@B@@CBCAA@I@EAC@A@@BAB@@@B@@BB@B@BB@@F@B@BBDB@BBB@B@@ADABEDCDCD@BBBBBDAD@HEHEDCDC@E@C@A@A@C@@@A@C@C@ACE@A@@@A@@B@D@B@DBB@BB@B@D@BB@B@B@D@B@D@@@@A@@@AAEAAAAAAA@AAC@CAA@@@@A@C@C@ABA@A@AB@B@F@@@BA@@AAA@CAAAAAA@@@CBCBAB@@AB@BBD@B@B@@ABC@A@CAA@@@AAAC@@@A@A@C@C@A@C@A@@@A@AB@B@BBBBBB@@B@BABA@A@EBCAAACAAAC@A@@B@BADAHEDA@A@AAAA@CAA@@CA@@AAB@BC@A@C@AACAAA@@@@A@@@@@A@@A@A@@@ADAHEBA@A@C@@@A@@AA@@AAA@AAA@BBAD@B@BABCDA@@@CDAB@@@@@B@B@@@@C@A@@B@@@BA@A@@@@BAB@@@@@BA@E@@BEA@@AAA@@B@@CA@@C@@AA@@AB@@AD@AA@CB@@AA@@EBBAEB@AA@@@@AA@@@@ABA@@BA@AB@@AA@@A@@@A@ABA@@BAB@@AB@@AC@@AA@@@B@@A@AA"],"encodeOffsets":[[117918,33379]]}}],"UTF8Encoding":true});}));