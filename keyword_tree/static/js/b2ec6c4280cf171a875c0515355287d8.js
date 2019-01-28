(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('蒙山县', {"type":"FeatureCollection","features":[{"type":"Feature","id":"450423","properties":{"name":"蒙山县","cp":[110.525003,24.19357],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@B@B@@@@B@@B@@@@ABAB@D@@@B@@B@@D@@@B@@AAA@@@A@@@@@@B@@@BA@@B@@@B@B@B@@@BBB@@A@A@@@A@A@@@@BA@@B@@@B@@@BB@AB@@@B@B@@@B@B@@@BAD@B@D@BAB@B@B@@@D@@@AAB@@@@AB@@@AAB@@@@@@A@@B@@A@@D@@A@@B@@A@@BAB@@@@A@A@@B@@@@AA@@@@AA@@A@@@@AB@@A@ABA@@@A@A@@@@@@AA@@@A@@AA@@@A@@AA@AA@@@@A@@@@A@BA@@A@@A@AA@@@@@@@B@BA@@@@BAAAA@@@A@@@@@A@@@@@AB@@A@A@@@@BA@A@@AA@@@@@A@@AAA@AA@@@A@@A@@@A@@A@@B@@@@ACCBA@AA@@@@ABA@@@A@@@@AAAA@@@AB@@A@A@@@AD@@@@AA@AA@@C@A@@@@@@A@@@A@AAA@@@@B@@@@@B@@@@AD@@A@@A@A@@@A@@@@@AA@@@C@@AAA@@@@A@@@A@@@@@A@@@@@AA@@@@@@CA@@A@@AAA@AA@A@@@@B@@@@A@@@A@@@@B@@@@@B@@@B@@A@EBCAAB@@AB@@@@@BA@@B@B@B@@@@@BB@@@@B@BBBBBB@BB@BB@@B@BABA@B@@@@BBB@@ABA@@@@B@@AB@@@@@B@B@@@BBBA@@B@@@B@DA@@A@B@@@@ABA@@@@@A@@A@@A@@BA@@@@@@BB@@@@@B@@@@@BB@@@AB@@BBA@B@@@@@B@@@B@B@B@@@B@@@B@@@@@DBB@@@@@DB@@@@B@BA@@B@@@@@@AB@@@B@@AB@@@@@@@@@@A@@BA@@@@@@@AA@AA@AA@@A@@@A@@A@@A@@@@A@@@@AA@AA@@A@@A@@AAB@@AA@AAA@@AA@@A@@A@@@@@A@@@AA@@@@@@@A@@A@@@A@@@A@@@@AA@@A@@BA@@@A@@AA@@AAA@@@@A@@@AAA@@AA@AA@@@@ABA@@@@AAAA@@@@@A@@@@@@@@B@@A@@@AB@@A@@@@@A@@@AA@A@AC@AAA@AA@@@@A@A@@@@@@@C@@@@A@@A@@@@AA@@AAA@@@AA@@A@A@@@AA@@A@@@A@@AA@@@A@@@AA@@@ACA@@@A@@@A@@C@@@@@A@@@@A@@@@@A@@@@@@@A@@@A@A@@BA@A@@@AA@A@@AA@@A@@@@AA@@AB@@@@A@@@CA@@@B@@@B@@A@A@@BA@ABA@A@AB@@A@@@A@@@@BA@@BA@A@@AA@ADA@A@A@A@@@@@A@@@@@ABAA@@@BA@A@@@A@AA@@A@@@A@A@@@@@ABA@A@AA@@A@C@AA@@A@@@@CAA@@A@@A@A@@@@@AA@@AADA@A@CB@@A@@@AA@AA@@@A@AA@@A@A@A@A@@BA@A@AAA@A@@@A@@@@@A@@BA@A@@@ADCB@A@@@ABA@ABCA@@A@@ABA@@BAB@B@@AB@@@AA@@@AA@A@@@@AC@A@@@@@@@A@@BA@@A@@@@AA@@A@@@@@AA@@@@@AB@@AA@@@A@@@A@@AA@@@@@A@CCAA@AA@@A@@@A@ACA@AA@A@@A@@A@@@A@@A@@BAA@@@B@B@@@@A@@B@@A@@BA@A@@@@@@BA@@@C@@@AAAB@@A@@@@AA@@@@@@@A@@@@@A@@@@@A@@BAAA@A@@@@B@@A@@@@D@@@@A@@@@BAB@@@B@@@@A@@@@@@@AA@B@@@B@@A@@B@@@@@@A@@BB@@B@B@B@@A@@@@BAB@@@B@@@@@@AB@@AB@@@@AB@@@BA@@BAA@@@@@@@@A@@@@@AA@@@@ABA@@AA@@@A@@@@@@B@@@@@@A@@BA@A@@B@B@@@B@B@@@@AB@@@@A@ABA@A@@@@B@@AB@@@@AB@@@@ABA@A@@B@@@@A@@@@B@@A@@@@@@B@@A@B@AB@B@@@B@@@@@@@BB@@@BB@B@@@B@@@@@@AB@@BBBB@@@B@BB@@@AB@@@BB@@@@BB@@BA@@BB@@@@BB@@BB@@B@@@B@B@@@@@B@@BB@@@B@B@@A@@@A@AB@@AB@@@@CB@B@@AB@@@BA@AA@@@B@B@@@B@@@@@@ABA@@@@B@@@B@BA@@BA@@BB@@@@B@@@@B@@BB@@B@@@BA@@@@@AB@@@@@BA@@BA@@@BB@@@B@@A@ACA@@@@B@B@@ABA@@@A@@@@@@D@B@@@B@@A@@B@@A@@@A@A@@@@@ABB@@BA@@@@@@B@@@@@@AB@@@@@@@B@@@@@@AB@@@@@B@@BBBB@@@@@BAB@B@BA@@BCBBB@@BB@BB@AB@B@B@B@@@B@@@@@B@@ABA@@@@@AB@@@@AB@B@@@@@B@@@BA@@B@@@@A@@BA@@@@B@@A@@@@B@@@B@@A@@B@B@@@BA@@@@B@@@@A@@BA@@B@@@B@@A@BBAB@@@@@@@BABA@@@@@AB@@@B@B@B@@@B@@@@@BA@@@C@@@@BA@AB@@@@@BA@@@@B@BBBBB@B@@ABA@@B@@AB@@@BB@@@@@AB@B@B@B@@@@A@@@ABCBA@@@A@A@AB@@ABA@@@@B@@@@@@AB@@@BB@@@@BB@@@@B@@@BAB@@@@@B@B@@@B@@@@@B@@@B@BB@@@@B@@@@@B@@@B@@@BAB@@@B@@@B@@@B@@A@@@A@A@@@A@@@@@@@@@A@@@A@@@@@A@@A@@@@A@@@@@AB@@@@@@AA@A@@@@@@A@@A@@@@A@@A@@@@@BAB@@A@AB@@@@A@AB@@AA@B@AA@@@@AA@@@@@@@A@@@@@@@AAA@@@A@@@A@@@A@@@A@AB@A@@ABA@@@AB@@ABC@AA@@@BAB@@@B@@@BAB@@@B@@@@@BA@@B@@BB@@AD@BABAB@@A@@@@@A@@@A@@@A@@@A@A@A@AA@@@A@@A@AA@@C@@@A@@C@@@C@A@@@AAA@A@@@AA@AAAAAAACEG@AAAA@A@A@@AA@@AA@@@@AA@@@AAA@@@@@@@AA@@@@E@A@@@@@@@@AEA@@@B@@AB@AA@@@A@@@@A@@A@C@@@@@@@@AA@@@@@AA@@A@@A@A@@DABABA@AE@A@AAC@CAAA@@A@A@EA@@A@A@A@@AA@A@C@CBA@AB@@AA@BA@A@@@@@A@@ACBC@CDA@@@A@@BA@@@CB@@ABA@@@C@A@@@@B@BA@B@@BAB@@@B@B@B@@@@A@@@@DA@@BABABA@AB@BBB@B@B@@BB@@@@@BB@@@@B@B@B@DA@@@A@A@@@A@@@@@A@AA@@@B@@ABAB@BABB@@@B@@BBB@@BA@B@@BB@@B@@@BBBBB@@BBB@@@B@@BBAB@@B@@B@B@B@BA@@@A@@@@BA@A@@@ABABA@@@A@@@C@A@@AAA@@@@ABB@@@@BDB@@@@A@@@A@A@@A@@@A@@@CAA@@AA@@CB@@@B@B@@@@AB@@CA@@@AA@A@AAA@@@BA@A@@BA@@B@@A@@@A@@@@BA@@@AA@@AAA@@BAA@@@@@@A@@AAA@@A@@@AC@AAA@@@AD@BA@@B@@@@BBA@@BA@@BA@@@@B@BA@@BA@AB@@ABA@@@@@A@@BA@A@@@A@@@A@@@AB@@@B@@BB@@@B@@@@@B@@@B@B@D@@BBB@@B@@BB@B@@@@@@AA@@@@@@@@A@@@@@A@@@@@@@A@B@BA@@@@A@@@@@A@AAAB@@@@A@@@@A@A@@@B@@AA@@A@@@A@@@@@@A@@@@@@A@@BA@@A@@@@A@@@AB@B@@AA@@A@@@@AAAA@AAAAA@A@A@@A@BA@@BB@@B@B@BBB@@@@BB@B@@BB@@BB@@BB@@@BB@@@@@B@@@@B@@@@BB@BDBB@@@@DB@@@BD@@@@BB@@BB@@@@BB@@@@@B@@@@BAB@@ABABA@@BA@B@@@@@@B@@@@@B@@@@@B@@@@@@BB@@@B@A@@B@@A@A@AB@B@@A@@B@@D@B@@BB@@@@@B@@AB@@@BAB@B@B@@B@@B@BBD@@B@@@@@@@BB@AB@B@BA@@@A@@@@@AB@BAB@B@@@BA@@BAB@@@BA@@@A@@@@@@@@@A@@@A@@@A@@@@@A@@@@@A@@@@@A@@@@@@@@@@B@B@B@@AB@@A@@B@@@B@@BB@B@@B@@@BBBA@B@@@@BB@@@A@@@D@@@B@@@@B@@@B@@@@B@@@@@@@B@@@A@@BB@B@@@@@B@@@BB@@@@B@@@@@BBA@B@@@@@@@@@B@@B@@F@@@B@@@BB@B@@@@@BA@@B@@@B@B@@@B@B@@@B@@@@@B@@B@B@B@@BBB@@@@D@@@BB@BBD@@@B@@@B@BB@@@ABA@AB@@AB@@A@@B@@@@ABA@@B@@A@@@@B@B@@@@@AA@A@@@@@@@A@@B@@@@@@B@@@@BA@@@A@@@A@AA@@B@@@@@CB@AAB@@@@B@@BA@@A@@AA@@@@@@AA@@@A@@@@@@@@A@@B@@@DBB@B@B@@@BAB@@BB@@@B@@AB@@AB@@A@@@@A@@@AA@@@@@@@@AA@@@@@@A@@BAB@@@@AB@AB@@A@AA@BA@@AC@@@A@@B@@@B@@@@@@A@A@@@@@A@@@A@@BB@@BD@@B@BB@@@@@@BB@@B@B@@BB@BB@BB@@B@@@@AB@@@@@@BB@B@B@@ABBDB@AB@B@DA@@BA@BB@@@B@@B@@@B@B@B@@@D@@A@@B@@@@@B@@@B@B@@A@@B@BB@@D@BABBBABBB@@BB@B@@@@@BA@@B@B@@@@AB@@@@@B@@AB@@@@BB@DBB@@@@@B@@@@@B@@@@CB@@@B@@B@@@@B@B@@@@@@@B@B@@@@@B@@@@@@BB@B@@@BBBAB@@BB@@B@B@B@@@@B@@BB@@@@BB@B@@B@B@B@@@@@B@@A@@B@@AB@BA@@B@@CB@B@B@@AB@B@@A@@@@@@@@B@B@@@@@B@B@@B@@BA@AA@@@AA@@B@@@B@@AB@BAAA@A@A@@@A@@@ACA@@@@AA@A@A@A@@@@@@@A@@@A@AB@@@@A@@@@@@AA@@BA@A@@@@@ABA@@@A@AB@@@@@B@@BB@B@@@B@BA@@@C@A@A@@@A@@A@A@A@A@A@@@C@@CD@@A@A@@@A@@@@@@@@BABBB@@A@A@@AAB@BA@A@@@@AA@@@A@A@@@@E@@@A@C@@ABABABAB@@AB@BD@@@BB@@B@@BBB@@B@@@@D@BBAB@FABA@B@@BBA@@B@BADA@@BB@B@BB@BB@@@B@@@B@@@D@DAB@BB@@@@@BBBBBB@@B@@A@@@ABA@A@@@BB@@BB@@@B@@BB@@BB@B@@BB@@@@BA@@@@@@BA@@B@@@@A@@@@BAB@@A@@B@B@@@B@B@B@B@B@@@B@@B@@AB@@@B@@@B@@@B@B@B@@@B@B@BJFFDBBBBDFBBAB@@@@A@@@@BA@@@@BCB@AA@@@@@@BA@@BABAB@@A@@@@@ABADAB@@A@@@A@@@@A@@@AAB@@AB@@@@AB@@@@AB@@@@AB@@@@A@@@A@A@@@A@@@A@@@@@AAA@@@@@@@@BA@A@@@@BABA@@@A@A@@@A@@@@BAA@@A@@@A@@@A@@BA@AB@B@B@@@B@@@B@B@B@BAB@@@B@@@BAB@@AB@@A@A@@BA@AB@B@@B@@@B@@@A@C@@B@@A@@BABABA@@BA@AB@@@@A@@@A@ABAAAA@@A@A@@@A@@@A@CA@@AAA@@@@@CAAA@A@@@@AAA@@@A@@@@A@@A@A@@@@@A@@AAB@@AB@@A@@@AB@BA@@B@B@@BB@@CF@@AB@@C@A@A@A@A@@@@@A@@@@B@B@@@@A@@BA@A@A@@@@AA@@@@A@A@@@@A@A@@@A@@A@@AA@A@@@A@@A@@A@@ABA@@@@BBF@@BD@@@@@@A@@BBD@B@BB@@@@@B@B@@@@@@B@BA@@@AB@BAB@@@B@B@@DBB@@B@@B@@BB@@B@@@B@@BB@B@F@@BB@B@B@B@B@@@B@B@@BDAB@@@B@BAD@@A@@@@@@B@BAB@@@@B@@@B@D@BAB@D@BAD@B@BB@@ABAB@@@B@@@BA@@@BB@@A@@@AB@@@@@@BB@@@@@BAB@@@B@@B@@@@@AB@B@@@BB@@@CBA@AA@AA@@@AB@@@BA@@@@@@@@@@B@@@@AB@@A@@@@@AD@@A@C@@@A@@B@@AB@@A@@A@@A@@@@@AB@@AA@@@@A@@@@@AA@@@@@@@@@B@@@@@@AA@@@A@@A@@@@@A@@B@@@@@B@@@B@@@BAAA@A@AA@@C@A@CAA@CAA@GCA@EAA@A@@@@@@B@@@BBB@@@BB@@BA@@@@BA@@@AB@B@@BB@@BB@@@BAB@@A@@@@B@@@B@@@@@@B@@@BBBBBBBBABBD@@BBBB@@@@B@BDD@BBDBBDBDABBB@BB@@BBBB@FBB@BB@@D@@BABBBBDA@BDB@@ABAB@B@B@DB@CA@AA@AD@@BB@H@@FBB@B@BB@DBBDBCD@BABBB@BDD@BBBABABBFBB@BBDBBBD@@CBBBAB@AABA@AB@@@DABAD@FBCAHA@@@B@BBDD@DDBBB@@DBBBBB@B@BDD@B@@@DB@FA@@@BBB@@@B@@@B@B@BABBBADA@A@@AA@@@A@@@AB@@B@@@B@@B@@B@@@@@@BB@B@A@@@@@AAA@@A@@A@ABB@@@A@A@@@@@@@A@@B@@B@@@B@B@@B@@@@A@@@@B@@@A@@@AA@A@@@@@@B@@@BB@@@@B@@B@@@@@A@@B@@@@@@@A@@@@@@@@@@A@@@BA@AAA@@A@@@@B@B@@@@@B@@AB@@B@@@@@B@@@@B@@@@@@@@@B@@@A@@A@@@@@@B@B@B@@@@@@A@@B@@@@@@@B@@@B@BAFA@@@@@@@@A@@A@@B@@@@A@@A@@@@A@@@@B@@@@A@@A@@@@@@@B@@@@ABA@A@@@@AB@@@@A@BADA@@@A@@B@@AB@B@@@@@@A@@@AB@@AB@@AB@@@D@@@B@BABBB@B@@@@B@DABBB@D@@@ABBBABB@AD@B@@B@B@BB@BBB@@D@B@@@BAB@@ABABAB@@AFD@D@FBBAD@B@B@DB@B@BB@ABAB@B@@@BA@@DAB@BA@A@A@@BABA@@BA@@A@AAA@AAA@@@@ABA@AD@@@@AB@B@B@@ABB@@BB@@@@BBB@@BBBB@@@@BB@BA@BB@B@@@BB@B@B@DBB@BAD@D@DCCEDED@BAD@@GB@DAJA@ADABDB@DCBBDA@DD@@BABBBABA@DF@BDBBD@DABAB@DB@B@B@BBDBDBDADABDBFC@@D@B@BBBB@@BDDBD@BFDBBDBBB@DABDB@BDBBJ@@B@DAB@AD@BAHBBD@DBHBB@BDBABBDADB@GAC@E@C@CAAFCBIACBACAAGABBE@ADEDIHAB@FBFGF@B@@AB@@@B@@@@A@A@A@@@@BAB@@@A@@ABCA@BA@A@@B@@BB@B@BABA@A@@@AB@BA@@@@@@@A@@AABCAE@@@A@AB@@AAAAA@A@@AA@@@@@@@ABAA@@@@A@A@A@@@@@AA@BA@@A@@AAA@@@A@@B@@A@@@@@A@A@@B@B@D@B@@@DA@@@B@@B@@@B@@@BAB@@@@@@@B@@@@@B@@@B@@A@@@@@@B@@@@@@@BB@@B@BB@@B@@@B@BA@@BBBBBBB@@@BBB@B@BAB@B@B@BA@@@AB@@@B@D@@@@@B@@@@@@@@AB@@@BAD@B@@@@@B@@@@@@AB@@@@AB@@C@@@ABAB@@@@@@A@@@AB@@A@@@@A@@AA@@AA@ACAAA@AAA@AA@@A@@@AA@@BA@@@AA@@@@C@AB@@A@AA@@@@A@A@A@@A@A@@@A@A@@A@@A@@@@AA@@@@@@A@ABA@@BA@@@AAA@@@A@@AAA@@AB@@A@AAC@@@@AA@@@AA@@A@@@A@BAA@@A@@@@A@@@@BA@@@@@@BC@A@@@@@@@A@@@@@@@A@@A@@@@@AA@@@@B@@AA@@A@@A@@A@@@@@AB@@@@A@@A@@AA@@@@@BCB@@@@@@A@@@AB@@@D@BA@@@@A@@A@@ACBA@A@@AA@@@@@@@@DBBB@@B@@@BAB@BAB@@AB@@@@@@@@@@@B@@@BBB@B@B@@@BAB@@@B@@BBA@@@@B@BABAB@@A@@@@@@@A@@A@@@@A@@@@@@@@C@@A@@@@@A@@A@@@@AA@@@A@@@BC@A@@@@B@@@@@@@@AB@@C@@BC@@@@B@B@@A@@BA@@@@DA@@@@@AB@@@@A@A@@AA@A@A@@@A@@BA@B@A@@@A@@B@@@BA@@@@@@@A@@B@@@B@@BB@@@B@DB@B@@D@@@BA@@B@@AB@B@@AB@B@@@@@BA@AB@@@BA@@B@BB@AB@B@@BB@@@B@@@@@@@B@B@BAB@BA@@@@B@@@@@B@@A@@@@B@@@BA@BB@BA@@B@@@@@B@@@BAA@@@BA@@@@B@BB@AB@BB@BB@BA@@B@B@BAB@@@@@@AAA@A@@@AA@@@BA@AB@AA@@@@@A@@@@D@@AB@AA@AB@@@B@@@@@BAB@@AB@@A@A@@@@@AB@@AB@@BB@@BB@B@B@B@@BBB@@@@B@B@@B@@B@@AB@@@@@@@@@@AA@@@AAAA@A@@AA@AA@A@AAAA@@@@B@@A@@@@@AB@@@BA@@BA@A@@BA@@AAB@B@@@B@@@D@@BB@@@@AB@@@D@@@@A@BBA@BB@@@@@@BB@BB@@@A@@D@@@@@@A@@BAB@@A@@@A@A@AB@B@BA@@B@@@B@B@@@B@@@@@BA@@B@B@@@@AB@@@@AB@@@@A@@@@@@@A@@@A@@B@@@BAB@BA@@@A@A@@@@@@A@CA@@@@@@@A@@@A@@@@@@AA@@AA@@A@@@@AA@A@@A@@@AB@@@AA@@@A@@@A@@B@@@@@@A@@@@AA@@@@@A@@@A@@@@@A@@@@AA@@AA@@@@A@BAA@@@@A@@@@AA@BA@A@@@@@A@@@CB@@@@@@@@AA@@B@@@@AAA@@@ABA@A@@@@@A@@@@BA@@@A@@AA@@@A@A@@AB@@AA@@A@@@A@@A@@@A@@A@A@@AABAA@BAA@BAA@@@AA@@BAAB@@AA@@@@@@B@@AA@@@@@A@ABA@@@CB@@@BA@@@A@A@A@A@@@@@@A@@A@A@@ABA@A@@@@@@@A@@@A@A@@@AA@@AB@A@@@A@@@AAA@@@A@@A@@@A@BA@@@@BAB@@@@@A@@ABA@@@CB@@@@A@A@AB@@@@@B@AA@@BA@ABA@@@AB@@@@@@@@@@A@@@@@A@@BA@A@@@A@@BAA@@@@@AA@A@@A@@A@@@@@@@@@CAA@@@AAB@A@@@A@@A@@A@@A@@A@A@@@@A@@A@A@@@A@@@@AA@A@A@@@A@@@A@@@@@@@@BA@@@@@A@@@A@A@@@AAAAAAA@@A@@AA@@@@@BA@@AA@@@C@@@@@@C@@@@@@@@A@@@@A@@@@A@@AA@@AAA@AAA@@@@AAA@AB@BAB@@A@@BC@@B@@@@@BA@A@@@A@@B@BABAB@@@DA@@@AB@BA@A@ABABA@AB@@AB@AA@A@@@@AAA@@@AA@@@A@A@@B@@@@@D@@@B@BB@@B@@@@@B@@@B@@@B@@@@AB@@AB@B@BA@@@@@AB@@ABA@@@@F@@@B@@@@AB@@@@A"],"encodeOffsets":[[113365,24607]]}}],"UTF8Encoding":true});}));