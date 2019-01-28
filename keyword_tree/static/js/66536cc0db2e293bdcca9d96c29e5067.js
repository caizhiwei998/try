(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('鱼峰区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"450203","properties":{"name":"鱼峰区","cp":[109.452442,24.318516],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@A@@GIAAAACAAAAEA@@A@C@AAE@AABA@A@AB@@@CA@A@AAA@A@ABA@@@@AAC@@@A@A@@AAAAAA@@A@@A@AA@AA@@AAA@A@AACA@@AAA@@E@A@A@AE@@DABAB@B@@CBAAA@A@@@@@A@C@@A@@@AB@BCB@BA@@@A@@@@@@@@@CECA@ABC@EB@@@@@AAAEBA@CBA@C@A@CDABCAED@@@D@B@@GCA@ABCB@B@BA@A@@@@@@B@@@@AB@B@@@B@@B@@B@@@BB@@BB@@@BBBB@B@@@@BBB@@BB@BB@BABCB@@AAAB@B@@@BADBD@@@B@@@@A@FBD@@B@B@DBB@B@@FDDBB@BHB@@B@B@BBBADA@CD@BCBIDABABADC@ABBB@@@B@BC@ABBB@BB@@BCBBBBB@B@@@BCB@DBB@@@FB@B@@@@BB@@@@@@@@@@@B@BB@B@@@@ABA@BB@@@B@@@@@B@@@@@B@@A@@@@B@@@B@B@@@B@@@@DA@@@BBB@B@@@D@@@@@@D@B@B@@@DBD@DD@@BB@@DD@B@B@@DB@B@@BD@BAB@@@BB@D@@@@@D@DBB@N@@@LBB@H@B@@@B@@@BI@ADMR@DAB@HEBBLPFHHLHJFHHRBDBHFJ@FBF@B@DAL@H@FAL@D@DBH@B@@FH@DFJHF@@HDFDD@DFBBBF@B@B@FCDCHEDCB@@GBA@@@@@BDB@@B@@A@@B@B@@@BB@@BB@@B@@A@@@A@@@A@@@@@@B@B@BA@@BB@B@@A@@@B@@@B@@B@@AB@@@@B@@AB@@@@B@B@@@@@@BA@A@CA@@@@ABBB@BBB@@A@B@@@B@@B@A@@@@BA@@A@@BA@@A@@@A@A@@@@B@DB@AB@@A@@@@@@@BB@@@BDBB@@@AB@B@@@@BB@BADB@@@ABAB@B@@@BCDABAB@@@DB@@BA@AB@BAB@B@@BBB@AB@@@AB@@@B@B@@B@BB@@BB@B@@@@@B@B@@@BABB@@@B@@@@@A@@@@B@@@B@BFD@B@@B@B@@@@@A@@B@@@@DB@@@@BA@@@@B@@@ABA@@@@BA@@B@B@B@@@B@@@@@B@@BB@@@BB@BFB@@B@@@BB@@BBB@@B@@BB@BBBBBB@@BBDBB@@BB@BB@@DB@@@@@B@B@B@B@B@@B@BBB@@@@@BBA@@BBB@@@BDA@@B@@BB@B@BAB@@BB@B@@@@@@@@B@@B@@B@BB@@BB@@BB@B@@D@B@@@B@@CDA@A@@@@@ABCB@@A@@@AA@@@B@@@@AB@@@@@@@AA@@@A@@@@@AA@@A@@AAB@@@B@@A@@@@B@B@@BB@@AB@@A@@@@@@@@BABA@A@@@EDCBB@@D@BB@BBA@BB@BBD@BBB@B@BBBC@ABAB@B@B@ABD@@@@B@BB@@B@B@@D@@AB@B@B@BB@BB@@B@D@D@@@BB@@@AB@B@HCB@@@DBB@@@@@B@@@BBD@BBB@BBBBBBBBB@@B@@B@DE@AB@@@B@@@@BB@@@B@@@BD@ABB@@@@@B@@@BB@@@@B@@@@AB@@@BA@BBBBB@BD@@B@@BBBBDBBDB@B@@AB@@@BBB@@@D@@@D@DCBB@@B@BB@@BD@B@BCDDF@FDBBDBBBBBFDH@HAAABABADCBBDDFCBC@AB@B@B@B@DADCDC@ADDBA@@BCBEBAB@D@DA@@DABA@AEC@AAAAA@A@@@AA@@AAA@C@A@AA@@@AA@A@AAA@C@ADCBA@A@A@A@@@A@@@AA@@@AAAAA@@@@@BC@@BA@@@@@ADCBA@@@@BCB@B@@AB@B@@@@@@C@@@A@@A@A@@@A@@@@B@@A@@AAA@@B@@A@@@@@@@@BA@@D@@@BAAA@@@A@AD@@ABA@@@@@A@@@ABA@@BA@@@@B@B@B@@B@@@BB@@BBA@@@CBA@A@@@@@A@@@A@@@A@@@@@A@@@@A@@AA@@@ABA@BA@@@A@@AAA@@AB@BA@@@A@@@@@AAA@A@@@A@@@AB@A@@CA@AAAAA@@@A@@@@@A@AACC@A@A@A@CAACC@@@@A@@@A@A@@AA@CC@AA@A@@A@@@AAA@AA@@@ACAA@A@@@A@@A@@@AA@@AA@@@A@@@A@@B@@@@@BA@A@A@@B@B@@AB@B@@AB@@@@A@@@@A@@@A@@@@AA@AA@A@@AA@A@@@@BABC@@A@@@A@@A@@AA@A@@@A@A@A@@@A@@@A@C@@D@@@@AB@@@@AAAB@@@@A@@@@B@BAB@BABADAB@@@BABA@@B@@@BA@@@@@B@@BB@@B@@@@@@@@@BA@@@A@@@A@@@@@B@@@@@AB@@@@@@@@@@@@A@@@@@@B@@@@@@B@A@@B@@@@@@@B@@B@@@B@@@@B@BA@@B@@@@@@@@@@B@@@@@B@@D@B@@@@@@@BB@@B@@@@A@A@E@@B@@@BB@BB@@@@@BA@A@@B@B@B@@BBA@@BA@@B@B@B@B@@AB@BB@@@@@A@@@@@A@@@@A@@@AA@@BA@@@@D@@@@A@AB@@A@A@@@@B@@@@AAA@@@@AA@@B@@@A@@@@AAAB@@@B@@BB@@@@@@@@@@@BA@@B@@A@@B@@B@@@@@@@BAB@@B@@@@@@@@A@@@ABB@@@B@@B@@@@@B@BABA@ABA@@@@@@@@@AA@@@@@AB@@AA@@@@@@ABACB@@@B@@A@@D@@@@@@@A@@A@@@CA@@A@@@@D@@@@@@@BB@@B@@@@@BA@@@@BB@@@CAA@@B@@@B@@@B@@@@@@@@A@@@@B@@A@@@@@@A@@@A@@@@@BA@@@@@@B@@@B@DA@@AAAC@A@ABABEBC@@AAAAAA@@AA@A@AA@@A@@@@@CA@@A@@A@E@@@@B@@@@A@AA@@A@@@@A@@A@@BA@@B@@A@AB@@A@AB@@AA@BA@@@A@@@@@A@@@@@AA@@A@A@@@@A@@@CA@@@@A@@A@A@@@@@@@@A@A@@@AAB@@CA@@@@A@AB@@@AA@@@@AAA@@@@@@@@@A@@@@@@AA@@@A@@BA@@@@A@A@C@A@@BA@@@@@A@A@C@@A@@@@B@@@AA@@B@DA@@B@@@@AB@@@@@@A@ABA@AAA@@@@@@AAA@A@A@@@@@AAA@A@CAAAC@A@@@C@@A@@@@AA@AA@@A@@A@@@AAA@A@ABA@AAA@@AA@A@@@@A@@A@@@@@@@@A@@@A@A@AB@@A@AB@BAB@@@@A@C@@A@@@B@@@B@@@@@B@@@BBB@@@DA@@AC@AAA@A@@BAB@BBB@@@@@B@B@@AAA@@A@@@@@@@@@@@@@@A@@AA@@@@@@AA@@@B@@@@A@@@@A@@A@@@@BAB@@@A@@@@@A@@AA@@AAA@AAAA@BA@@@A@A@@@AAA@@A@@@A@A@@A@A@@B@B@@@@BB@@@@BB@@BBBDB@@@@BBFB@@@AB@@@@@@AAA@C@AAAA@AGD@@ABABA@@@A@@@@B@B@BA@@BA@@B@@AB@A@@@@@@A@@B@@@A@BAA@@AAA@@B@@@@A@@AA@@@AA@AA@@@@@@@@A@@@A@@A@@@A@AB@B@@@@E@AB@@@@A@@@@@@@AA@@EAA@@@A@@@@BA@AB@@@BA@A@@@@@A@A@A@@@AB@AA@@@A@@@@@AB@AAB@@A@@@BB@@@B@BAB@BCB@BCB@@@ACA@@A@ABAA@@@@@B@@A@@@@@A@A@A@@@@@A@@@@@@@A@@@AB@@@@ABABA@@@A@@@@B@BAB@@@@@@@B@@A@@@@@A@@B@@AAABA@@BA@@@@@@AA@@@@@A@@@A@@BA@@@ABABA@ABAB@@A@@@ECA@@AC@@A@@AAA@@AA@AA@@AA@@AA@@@@AAA@@A@@AAA@@@AA@@@@@@B@AABA@@@A@@@@@A@A@@@@@@C@A@A@@@BC@E@@CA@@A@AAA@@A@@AA@@@@@A@@@AAA@@@AA@@A@@AC@@@@BAB@@A@@B@BA@@BA@@@A@@BA@AB@@@@@B@B@DA@@BA@@@A@@@A@@@A@@BA@ABC@C@EBC@@@@@AA@@@@AA@@C@AAA@A@@@A@@A@@A@@A@C@@@@A@A@AA@@@AAAAAA@@A@@AA@@A@@A@@ACCACA@A@EBA@A@A@C@ABC@@B@B@@@@@BB@@B@BABA@C@CB@@AA@A@CBA@A@AA@@A@@@@@@@@AA@@@AAA@@A@CCAAAAAC@AA@@A@@@AA@C@A@@@AB@@A@@@A@ABAA@BAA@A@@@@@AA@A@@@@A@A@AA@@@A@@@AAA@@@"],"encodeOffsets":[[112118,24838]]}}],"UTF8Encoding":true});}));