(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('濠江区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"440512","properties":{"name":"濠江区","cp":[116.726973,23.286079],"childNum":2},"geometry":{"type":"MultiPolygon","coordinates":[["@@@BB@@@@@@A@@@@@A@@A@@@@@@@AB@@B@@@@@"],["@@CBSBOCC@SGAAUSkbCB@BEDCBEDA@IFCBCB@B@B@BAB@@ABA@@B@@ABAB@@@BB@B@B@@BA@ABAB@B@BA@A@@B@@@@@@BB@B@@CBABA@@@A@CBA@AAAB@@@BC@A@@BAA@@A@AB@B@@AB@@A@A@@@@B@@@BA@AB@BAD@BAF@@ABA@@@A@@@ADAD@@B@B@@@AB@@A@A@@@@BA@ADA@AB@@AB@@ABAB@@AB@BA@ABABAB@B@B@@D@B@@BB@@BBB@BB@B@BB@@@B@B@@B@@B@AB@B@@A@ABBBB@@BBBD@BBB@B@BAB@@AB@@AD@@@D@@A@@@ABB@@B@@B@@@@B@@@BB@@B@BA@AB@D@HABC@C@C@CCC@CD@BAznWJEHDBB@@HDLHPHB@JBDBLBPALArKJ@F@TBNAJEFEDCH@HAFAHCDGDCROLK@AF_HMBG@@@G@O@CBKFSFEDAFALBJAFAHCDEBE@IAGGQGSOMQCSB]H[N[H"]],"encodeOffsets":[[[119609,23809]],[[119549,23772]]]}}],"UTF8Encoding":true});}));