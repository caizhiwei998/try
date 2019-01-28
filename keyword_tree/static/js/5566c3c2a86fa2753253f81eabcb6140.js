(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('新青区', {"type":"FeatureCollection","features":[{"type":"Feature","id":"230707","properties":{"name":"新青区","cp":[129.533599,48.290455],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@FARCZMBCFEFCRCDABOAAIEOKs[GAG@ULE@KLMJ_PkLcNKLERKZSbgdi`SNANDZDVAN@NI`SnIhIzC\\OT[LeRWJOFABIDCBA@ABmRA@_Z]`ABQ^_lGPgzLBvNrF\\@VCTERCZBnJvTfFjAB@H@AbDhH\\HdNXH\\DjFbBVAVKPILEL@JHTP^JX@`ERARDBqBCHCHErFFACiCEECICI@OWAM@KBEPKDCFE@AIKQMGCAEACBCBAEEEAIEEGAMFIDMAGMMIOKIIEMCMAKDO@SCgUCC@CBCJGZMLKFIBWCKGMAG@EBGJIBGCC_SACBEDEJA@CACQIIOUQOGIEcEE@EEIQ@GBEFGNEHA@C@AEAIODEBK@GCGAEDEFUBSAGECIIAAB@"],"encodeOffsets":[[132852,49180]]}}],"UTF8Encoding":true});}));