(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('桐乡市', {"type":"FeatureCollection","features":[{"type":"Feature","id":"330483","properties":{"name":"桐乡市","cp":[120.565098,30.630173],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@@A@EA@@A@@@@A@@A@A@@@BG@@@@@@@A@@@@@@@A@@@@A@@@@@@BA@@AB@A@@@@@A@@@@@A@@@A@ABAB@@A@A@A@@@EE@@@BA@@@A@@@@@@@@A@@@@@AA@@BA@@@@@A@@@@@A@@@@@@B@@@B@@B@@BB@@@@@AD@@A@@@@B@BA@@B@@@B@@@@@@@B@@B@@@AB@@B@B@@@@@@B@B@@@B@@@@@@@@@B@@@@@BA@@BB@@@@@A@@B@@@@B@@B@@@@@BA@B@A@@B@@@@B@@B@@@@@@@B@@A@@B@@@@@@@@@B@B@BA@@@@@@B@B@@@@@@@B@@ABB@@B@BAA@@AD@B@@@BA@@@@BAA@@AD@@@BB@B@@H@BAB@B@BA@A@@@@D@@@BAB@@@BC@E@A@A@@A@@@@A@A@A@A@@@@BA@C@AAA@C@C@@@@@@@AB@@@@@B@B@@@@BB@@@@A@@@@@BB@@@@@D@@@B@@@@@@@B@@A@@B@@@B@@@@B@@BB@@BAB@@@BB@@@@@@@@@B@@B@@@@@B@@B@@F@@@BA@@@@@@@A@CJ@@@A@@@B@@@@@B@@@BAA@D@@@@@B@@@@BA@@B@B@@@@BA@@@@@@B@@B@@D@@@@@B@B@AAD@@@B@BAB@B@@@B@@@@@@@@@@@BAAAB@BAB@B@@@@@@@@@@@BB@@@@@@BB@@@@A@@A@B@B@@A@@B@@B@@@@@@@@B@@BB@@@@CB@B@B@BB@B@@@@B@@@@B@@@@@@@@@@@@@B@@@@@@@@B@@@B@@@A@@@@@A@@B@@B@AB@@@@@@B@@@@@@A@@@@B@@@B@@B@@A@B@B@@@B@@@@@B@@B@@@@@@@@@@BB@@@@@@B@@@@@@@@@@@@@@@@@@@@BD@@@B@@@A@@B@@@@B@@@@BA@@@B@AB@@B@@@B@@B@B@@@@B@@B@@@F@BA@AD@@@@A@CAA@@BCDABABCDEDGFAB@@@B@@BA@@@B@@@@@BB@@@ABB@@@@B@@@@F@@@@@@D@@@@B@@@@A@@B@@@@DC@A@AD@BB@D@B@@@@BABA@@B@@AB@@@@BBF@B@@@@B@@BB@@B@BBBB@@@@B@AAB@@AB@D@@B@@B@@AB@@@@@@A@@@@B@@BDA@B@@D@D@BBH@@@B@@@B@B@@B@@@BD@@@B@@@B@@B@@@@@@@@@BB@@@@@@B@@@BB@@@@@@@@@@@D@ABBBA@@BB@@@@@ABA@@@@@@@@BA@A@@@@B@BA@@AA@A@@@@B@@@B@@B@@@B@D@BAD@@B@B@@@D@BB@@B@@@@@@@B@@@@@@@@AB@@@@@B@@@@A@@BB@B@@B@@@BB@@@@B@@@@B@@@@@@B@@@B@@@@@@B@@@@DA@@B@@A@@BB@B@@D@B@@@B@@@DA@A@BFA@@@A@@DC@@@A@@@@DDABBA@@@@D@@B@@@BADABB@@@@@AB@@@@@@@@@@@BB@A@@@@@@@B@@@@@AB@@B@B@@B@@A@@@B@@@@@@@FB@@B@@BA@@@B@BBB@@BCD@@@@CD@B@@@@@B@@@AA@@@AB@@A@@@@B@@@@@B@@@@@@AB@@C@@@@DA@AD@@BB@A@@@@@@BA@B@@@@BB@B@@AA@@@@@B@@@@@@B@@B@B@@@@@@@BB@@@@B@B@B@FAD@@@BD@BBB@D@BA@@B@@@B@D@@@@@B@@@@@BFB@@@@BB@@@A@@@@@@@@@B@@BA@@B@BBB@BAD@B@@B@@B@@@F@D@@B@@B@@@@@@@@@D@@@B@DA@@@@@@D@@@@@BA@@BDBD@BBD@@@@DAHBD@B@B@B@@BD@BB@@D@BB@BB@@@BAB@D@BB@AB@B@B@@@B@@B@@@A@B@@@@B@@A@@B@@B@@@@B@@@@BB@@@@@@@@@@@B@@@@@@@@AB@@AB@@@@@@@@@@@@ABB@@@@@@B@B@@AA@@@B@@@@@@B@@B@AAB@@@B@@B@@@@@@AD@@D@DAB@@@DA@BA@A@@B@BB@@@BA@@AAD@@@DF@B@BCB@@A@ABA@AB@@@@@@@B@@A@@@@@A@@B@@@A@@AB@B@@@@@@A@@BB@@@A@@BA@AA@@@@@@@A@@AB@@AA@@@@AB@B@D@@@@@AB@B@@@@@@@@@@@B@@B@@@@AB@B@@@@A@@@@@B@A@@B@@B@@@@B@@@@@B@B@@B@B@@@@B@B@@D@@CF@@@@@@@B@B@@@@@@@D@B@B@@@@@@@B@@AA@@@@@@@@AA@@@B@@B@@DB@@@B@@@@@@BB@A@BB@@@@@@AB@@B@@@A@A@A@@@@BB@@@A@@BBBB@@@@D@@@BA@@BBHHFFB@B@@BB@@@@@A@A@BB@@B@@@@@BA@BB@@@@B@@@@@BA@@@@@BFDFFHDH@@BB@B@@CB@@A@@BB@@@@B@@@B@@@BC@@@A@@@@BAB@B@@AB@@@B@@@@@BA@@@@B@B@@A@A@@A@@C@@@AFBDA@@@@@@@@BA@@@A@@B@@@BB@@B@@@B@B@BB@@@@@@@@BA@A@@@@B@@@@@BB@@@@@@@B@@@@BADAB@BADAD@@BBD@B@B@F@D@BCB@B@B@@@BBB@D@B@@@BAB@BAB@DAB@BAD@B@DABA@@B@@@B@B@BDDBBDBBBB@@@@HJDDBB@@DFBDDFDD@BBBFFBDBBDHB@B@BABA@A@@@A@@@@@@B@@A@@@B@@@AB@@BB@@A@@@BB@@@@@BA@@@A@@F@@@@BB@@BD@@@@AB@BAFB@CFBF@B@@@BA@A@AB@@A@C@ABA@@@ABC@A@A@A@A@A@C@A@C@ABC@@@E@E@G@C@E@A@A@A@E@@@CJBD@B@B@@A@A@A@@D@@A@@@@@@@@BAA@@@@A@@@@@A@@@@@AB@BCDADC@@@@CA@@@AB@AAJGFDHEHIV_AA@@A@@@@A@@@@DBFDDBDBB@FD@@@ABAFG@@BABC@@@@BABABCDCDCBAB@@A@@F@@A@A@@B@F@B@@@@@@@@@D@@@B@@@@@@@@@B@B@@A@@@@@@@@B@@@@@@B@@@C@@@@@@A@@@BA@BBA@@@@@@@@@@BB@A@@@@@@@@@@@A@@@@@@@@A@@ABA@AEA@@AAA@A@B@@@BAA@@AA@@A@CB@@@B@B@@AA@@@A@AA@@@B@@@A@@AB@@@AA@@@@@@AA@@@A@@A@ABC@CAAAB@@A@@A@@@ADCGCAA@@@AAA@A@@B@@@@@@A@@@A@@@@@@@@@@@@@@@A@@@@@@@AB@@BB@@A@@@A@B@@@AA@@@A@@@@@@@C@@A@@@@@@@@A@@@@A@@B@B@@B@@@@B@@@B@@@B@@A@@@@B@@@@@@A@B@AB@@@@@@@@@@AA@@@AB@C@@B@@AA@@ABABC@AA@@@A@@@A@C@BA@@@@@A@@@@A@AA@@A@B@A@@A@@B@@A@B@AA@@@ABAABA@@AB@@@@@@@@@A@@@@BA@@@@A@@@@B@@@@@@@@@@@A@@@@@@@A@@A@@@@A@@B@@@@@@A@B@A@@@@@@B@@@@@@AB@@@B@@@@@A@@@@@@@A@@AB@@@A@@@@@@@B@@@A@@A@@B@A@B@@AAAC@@B@@@BCB@A@@@@@@C@@BB@@@IBCB@A@@@A@@BCAA@A@@@BA@@@A@@A@@@@@@B@@@@@B@@@@@@@@@@A@A@@@@@@@@@@@C@@@BB@@@@@@AA@@@A@@@BA@@A@BAA@@@@AD@@@E@@@@@@BA@@@@@@AA@A@A@A@@@@@@@C@@BD@@@@@@@A@@@B@@B@@A@@BAA@B@@@@@B@@@@@@@AA@@BC@@@BC@@@@C@@AB@@@A@@A@@@BB@@A@@@BB@@@@@BAAC@C@@@ABA@@BCBABCDC@@@BB@@@@@@A@@@@@A@@@@@@@ABB@A@@@@A@@A@A@A@@@A@@B@BB@@@C@@BA@EBA@A@ABA@CB@B@@BBA@BD@@@B@@AB@@@B@BAD@B@@BBB@@BAB@@@@B@@@@@@B@@@A@B@@@@@@@BA@@B@@@@@@@B@@C@@@BB@@@@@@A@@@A@@@D@@@@@@@B@@@@BA@@@@@@@B@@@@@@@B@@BA@@@@@@BABBB@@@BCBC@@B@@@@@@AB@@@B@FD@A@@AA@@@A@A@A@@@A@@@@B@@@@A@@B@B@@@@@BABB@B@@B@@@BBB@@A@AB@@ABCC@@@AAA@@@DE@@D@@@@@B@BA@@BAAAB@@ABABAC@B@AA@@DA@@AA@@@@B@@A@@@@@A@@D@@@BABA@@BA@@BCA@CAEAA@AAA@CA@@BC@CBA@ABA@AC@A@AA@@@@@A@A@@BC@A@@@C@@@BA@A@C@A@A@@@@@C@A@AA@@A@A@A@@@C@A@@@@@E@@@@A@@A@A@E@@@@B@AGA@@@B@@A@@@@A@@@BA@@A@@@@A@@@@@C@@B@@@@A@A@@@@@AB@@@@@@C@A@E@A@A@A@A@AA@@AB@@@B@B@B@@C@@@@B@@@B@@@AA@@@A@@@@@@A@@@ABA@A@A@C@@@@@AAA@@BC@A@A@@A@A@A@A@A@@@A@@@A@AB@@AB@@A@@@A@@B@@C@@A@@C@@AA@@AD@@@B@@@B@@A@A@@@AB@@A@@@@@@@A@@@@A@A@@@A@@@C@@@@A@@A@@@@@@@A@C@@@@@@@@@AA@@@@@B@@@@A@@@@@@@@@@@@AC@@@@B@@@B@@A@@@@BA@A@@@@@@BA@BAA@@@@@@@BAC@@@@@@@@@A@@@A@C@AA@@@@@A@@@@@@A@@A@@@A@C@EC@AC@AC@AAAACAA@EA@A@@@@@AC@@@@@A@@AA@@A@@B@@@@@B@@@B@@ABA@A@@@AA@@@C@@@@@@@B@@A@@@@@@@@AAB@@@@@@CB@@@@@B@@@BA@A@BAA@@@@C@@@@@@A@@@@BAFBBC@ACA@ABB@@BA@@B@@@A@@@AA@AKAE@C@G@I@A@C@EAAA@@@@@@@AA@A@A@A@@@@@@A@@@B@@C@A@@DO@CAK@@FA@@FC@@BA@@B@@EAABB@@@@@@@@BA@@@@@@@@@AHA@@@@@C@@B@B@@@@A@@@@@@@B@@D@@@@C@@A@@@AA@CA@BA@@AB@CA@@@@AA@@C@C@E@A@A@C@C@@B@B@@@@A@@AA@@@@DA@@@@@@B@@@B@@ABA@A@BB@@@@@@AB@@@B@@@@AB@@@@@BE@GA@@A@@A@@@A@@@AA@@@@@@C@@BA@CA@A@@@@@@BA@@@@BE@A@@BA@A@A@@A@@B@@@A@@@@AB@A@BAA@@@AAA@@BAA@@ABA@@@@@A@A@@@A@A@@@@@@@A@@@@@A@A@@@@@@@@@@@@@@@A@@@A@@@@A@@@A@@A@@@A@AAADAFADAFA@@AABA@A@@@@@C@@@@@@E@E@A@A@@@GC@@AB@@A@@G@@@@@@CC@@A@@@@@CKDC@A@@A@B@AA@@@@@@AA@@A@@A@@@@B@@@@@BA@@@@DKBGDA@GB@A@@@B@BAA@@@@@@@@@@@BC@ABA@AB@@A@@A@AA@A@@@A@ABA@@@EAAA@BABGCBCA@@C@@@CA@@A@@B@@@@A@@B@@A@@BA@A@@@@AB@@@A@@@@@@@@AAA@@@A@@A@C@AA@@@@@@@CCA@A@@BA@A@@@@@@BB@@@@@@BA@@@@@@BAB@@@BA@@@A@@D@@A@@@@@@BB@@@C@A@@@@@@@B@@AA@@@@@B@@@A@A@@@A@@@@A@@B@B@@@@@C@@AB@@@A@@B@@A@@@@A@@CA@@AA@B@@AB@@@BA@@@@AE@@@@@"],"encodeOffsets":[[123240,31211]]}}],"UTF8Encoding":true});}));