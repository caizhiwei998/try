(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('昌江区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"360202","properties":{"name":"昌江区","cp":[117.18363,29.273565],"childNum":5},"geometry":{"type":"MultiPolygon","coordinates":[["@@ABBBB@@@@A@AA@"],["@@B@@@@@@@@A@@@@@@@@@@@@AAAB@BA@DB@@@@@A"],["@@@@@A@@@ABA@AAA@@@A@@@A@@A@@AA@@@@CAA@ABAACAAA@AA@@@AA@@@AA@@@A@@@CA@@A@AB@@@AE@@DABA@@DCBA@A@@@@AA@@@A@@@A@C@A@@AAA@@A@@A@ABADADABAB@@B@BBA@A@EAA@@BC@@D@DAFADABABC@BD@D@@AD@BCBA@AB@BABBABBBB@@@BB@@AB@B@B@@@BFA@@BB@@@@@B@BB@@B@BB@@DB@@@@BB@@BBB@BB@@B@@@@B@@BBB@@@FC@BD@DAB@@@"],["@@AAAC@@@@AAA@AA@@A@@@AAA@A@@@@@@A@@BA@A@@@A@C@@@@@A@A@@A@@AA@@AA@@AABC@A@@@A@@BA@@B@@AB@@@@A@@@@A@@@@@@A@@@@AA@@@@@A@@@@@A@@@A@A@AA@@@A@@@@A@@@@A@@BA@@@@AA@@B@@@@@@@@@@A@@@@@AA@@@@@@@@@AA@@AACC@@@BA@@@@@A@BA@@@@@A@@@A@ABA@@@AA@@@A@@@@@@@AA@B@ABABA@@@@B@@AA@@@@A@A@@@A@@A@@A@@@@A@@A@@@@A@@@@A@@AA@@@A@@@@A@@@AA@@@@BA@AB@@A@@@A@@@AAA@@@@@AA@@@@A@@AABABA@@@C@@@A@ABA@A@@A@A@A@@@@A@@@@A@A@A@@@@@@A@AB@@A@@@AAAA@@AA@@B@@A@@A@@A@@@@@@@A@@@A@A@C@@A@@B@@AB@@@A@A@@@@@@@@A@@A@A@@@@BAB@@AB@@A@@@@@A@@BAA@@B@@@A@@@@@@@@A@@@@@@A@@@@B@@@@B@@@@B@@A@@@AB@@A@C@ABA@@@A@@@AA@@A@@BA@@B@@A@@@A@@@A@@BA@A@@@A@@@@A@@@@@A@@@@A@A@ABA@@@A@@@@A@BC@A@CD@@ABCB@B@@@B@@@B@@ABA@A@@BA@@@A@@@AA@ABA@@@CAC@AA@@A@@@@AA@@@@@ADA@A@A@A@@@A@@@A@@@A@A@AAA@ACA@@A@AA@@@AAA@@@@A@@@AA@@@A@AB@@A@A@@@C@@@AB@@A@@@@@@@A@A@A@AYM@@@AA@@@A@@@@A@@AA@B@AA@AB@@@@A@@AA@@@@@A@@@@@AB@@@@AB@@AB@BABA@@BA@@BAAABA@@D@@A@AAAAAAAA@C@@@A@@A@@B@B@B@@A@@@@B@@@@@DB@BA@@@@BD@B@@@B@@@BA@@@@BA@AD@@@BCB@DAB@@A@@B@@A@A@ED@@A@C@A@@B@@A@@BABABBB@B@B@B@B@@AD@@@B@@A@A@@BA@@@A@@DA@AB@@@BA@@@@BA@B@@B@@@@@@C@@@A@@@@BB@@@B@@@BBA@AB@@@@A@@@A@A@@@@B@@@DA@@@A@A@AA@@A@A@A@@@A@A@@BD@@B@B@B@B@@@BAAAAAA@@A@@BC@@B@@@@@@@BA@@@@A@@AACA@A@@A@@B@BBB@@@B@@@@@BAB@B@B@@@@ABBB@@A@@@@DA@@@A@@@@@A@@AA@AB@@@B@@@@@@@@AA@A@@AB@@AB@B@@@@@B@@A@@@@C@A@@AB@@AB@@@B@@B@@@@@@@@BA@@@@@BB@@B@@B@@A@@BB@B@ABA@@@BB@@B@@B@B@BBB@@AD@@@@@BEJA@A@EJCFA@@@AB@@A@@B@@@B@@@@@B@B@B@@A@@@BB@@@@ABAA@@AB@D@@@BC@@@A@AF@@@B@B@@@BBB@@B@@AB@@@@@@BBB@@@@@B@B@@@BB@@@@BB@BB@B@@@@CB@@@B@BAB@@A@@@@BABADB@@BA@@B@B@@B@@@BAB@@A@@B@@@B@@@BA@@@@@B@@ABAB@@B@@@BA@@B@@C@@@A@@BCB@@B@@@@@B@@@@@@@A@@BBABB@@@@@@BA@@BA@@@@B@@@@B@@@@B@@@BB@@@@BA@@@AB@@A@@@A@@@@B@@@B@@@@@BA@@B@@@@@BA@@BAB@@@@A@A@@@@A@@@BA@@@@A@@@@A@@@@@@@@A@@A@A@@@@BA@@BAB@B@@@@B@@@@@@A@@B@@@B@@@@@B@@@BAB@BB@@@@@@A@@B@@@@@BA@@@A@@B@BA@@B@B@@@@BB@@@@AB@@@B@@B@@@BB@@B@DBB@@BB@@D@@@B@@@@@@ABA@AB@@@@@BC@@B@@A@@@A@@AA@@@@@AB@B@@@@B@@@@@@BB@@BAB@@BB@BB@@@@BB@ABAD@B@@@B@@@@AB@@@BA@@BABBBAB@@@B@@@B@@@B@B@@@BAB@@@B@@B@B@@BB@@@@B@@@@B@@@BA@ABA@@B@@@@AB@@@@@B@@@@CBA@@@@@@@B@B@@@@@@B@B@@@BADAB@BA@A@@DA@@DAB@@@@@@D@B@@AB@@@@B@@BB@@@@@@BA@A@@@@B@@@@@B@AB@@@@@@B@B@@@B@@@@@@@BBB@@BA@@@@@B@@@@@@@A@@@@B@@BB@B@@@B@@@@@@ABB@@@@@@B@@AB@@B@@@B@@BB@@@@@B@@A@AAA@A@@A@@@B@@B@@@AB@@B@@@@@@@BBB@B@@@@@@@@@DB@@@@@B@@@BBB@BB@@B@@B@B@@@@@@@@@AB@@@@@B@@@@@B@@@B@@@B@@@@A@@@BB@B@@AB@B@@B@@@@A@@BB@@@A@@BB@@@@@@AB@B@B@@B@@A@@@@@AB@@@@@@A@@@A@@B@@@@B@B@@@@@@BA@A@@@@@B@@B@@@@@B@@A@@@B@@@@B@@A@@@A@@@@@@B@DAF@BB@@B@@@BB@@B@BA@@@@@B@D@B@@B@@BAB@@@@@BB@BBBB@@@AB@B@B@@@@AB@@@B@@@B@@@ABAB@@@@B@B@@@@@@@BA@@@BB@@@AB@@@B@BB@@@@@@@BA@BBA@@@@@A@@@@@@B@@BB@@@@@B@BB@@B@@A@ABADAB@@@B@@@@@@@BCB@@@B@B@B@B@B@@A@A@@B@@@@A@@@A@@@AB@BA@A@@@AB@@A@A@@@A@@@@@@AA@@@AA@@A@@@AAA@@@AB@@A@@DA@@B@@@DCB@B@BA@@B@BC@@@@@BB@B@@@B@@@@@@@BBB@@@@B@B@@@BB@@B@BB@@@@@BB@BB@@@@@B@B@@@B@@@@@@BBB@@@B@@@@@@B@@@@@@B@BBB@B@@@BBA@@@@B@@@@B@@B@B@@@B@@@@@BBB@@@BB@@B@@@BA@A@@@@BA@AB@B@@A@@B@@AB@B@B@B@B@BB@@@@BB@@B@@B@@BB@@@@@B@@@@@@B@B@@AD@@BB@@@@B@@BB@B@@@@BB@@BA@@BB@@B@@@@@B@@B@BBB@@B@@@@@@B@@@@@@BBBABBB@BBBBB@@B@B@@@B@@@B@@BBBBB@B@@@@@@@@A@@BB@@B@@@@@@@@@@A@@@AB@@@A@@BA@@@@A@@@@@@BA@@B@@A@@@BB@@B@@BABAD@DA@@B@@@@BB@@BBB@@@@@B@BBB@BA@B@@BB@DFB@B@B@B@B@@AB@B@@@BB@@@@BAB@BAB@@B@@B@BBJKBAB@@AAA@A@E@C@@BC@C@A@@@ABCBC@C@@@E@A@@@A@@BA@A@@BC@A@@@ABA@@@E@E@@@@BGBG@A@A@A@@@AAA@@@CEAC@C@E@@@A@A@A@ABA@AB@@AB@D@C@C@@@A@@@@B@@@B@B@@A@@@@@AAAB@A@A@@@A@@AA@@@@@@AB@@@BA@@A@@@A@@BAABA@@@@@@@A@A@BA@@B@@@@ABAA@@@AB@BCB@B@BA@@@AB@A@@@@@@@A@AA@@@@@AA@@@@@A@BAB@@AA@@@A@AB@@@@A@ABA@@@AA@@@@@@@A@B@@@@B@@@AA@@@@@@@A@@@A@@B@BAAAAAA@@@C@A@C@@@AA@@B@@AB@B@@@B@@@BA@@A@@@A@@@@@@@AA@B@@@@ABA@@@@@A@@A@A@AAA@@@@A@BABA@@@@B@@ABBBA@B@@D@@A@@B@@@@@BAC@@B@@A@A@@A@B@@A@@@@@AAB@@@@A@@@@@BA@@@@@A@@@@@A@@@@A@@@BAA@@@B@B@@@@AB@@@@@@@@A@A@@A@@@@@@BAA@@@@A@@@@BA@@@@B@@@A@@@@AA@@@@B@BA@@@@B@@B@@@@B@@C@@@@AA@@@AA@@@@@@AA@@@@@@@@@AAAFEJ@DCB@N@D@F@DCFAHBBADABBD@B@J@ADE@FBFBDDD@BCFI@E@GFQ@@@@"],["@@CCCCA@@@ADBB@B@B@B@@B@BB@@@BB@DDBC@A@A@@@A@@AA"]],"encodeOffsets":[[[120003,29960]],[[120091,30007]],[[120097,29998]],[[120032,29906]],[[120020,30030]]]}}],"UTF8Encoding":true});}));