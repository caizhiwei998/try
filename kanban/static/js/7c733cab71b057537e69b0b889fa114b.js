(function (root, factory) {if (typeof define === 'function' && define.amd) {define(['exports', 'echarts'], factory);} else if (typeof exports === 'object' && typeof exports.nodeName !== 'string') {factory(exports, require('echarts'));} else {factory({}, root.echarts);}}(this, function (exports, echarts) {var log = function (msg) {if (typeof console !== 'undefined') {console && console.error && console.error(msg);}};if (!echarts) {log('ECharts is not Loaded');return;}if (!echarts.registerMap) {log('ECharts Map is not loaded');return;}echarts.registerMap('敖汉旗', {"type":"FeatureCollection","features":[{"type":"Feature","id":"150430","properties":{"name":"敖汉旗","cp":[119.921603,42.290781],"childNum":1},"geometry":{"type":"Polygon","coordinates":["@@@A@@B@@A@@@@AA@@A@@A@@@@A@@B@B@@AB@@@@@A@A@@@@@A@@@@AA@@@@@@@@BA@@DA@@@AB@@@@AB@@A@@@AA@B@@@AABA@@B@@@BA@@B@@@@A@@@@@AA@@A@@@A@@@@@@BBD@@@@@@@@A@@AA@A@@@@AA@A@AA@@@A@@@A@@@@A@@@AA@@@@A@@@@B@@AB@BBB@@A@@@@@AAA@@A@@@A@@@A@@@@@A@A@A@@@A@@BA@@@@@ABA@@@A@@B@@A@@@ABA@@@@BA@@@AB@@AB@@A@ABA@@BA@A@A@@@CAAAA@@@A@A@ABA@@@@@@@@B@@BD@B@@@@A@AB@@A@AA@@AC@@AACCAAA@A@@@@@CB@BA@@@A@CAA@CAA@EAA@A@ADABA@ABAB@@@@AA@A@@@AAE@@ACA@AEAA@CBABAB@@@BA@A@@AAEE@@@@@@@@B@D@KEOAQA[OOBI@MDCBO@OBO@OCGMKKKIOCMAUEOSQICASIUIMCMIGEECEASIKBQDMHC@aLQMOQOGQIMCOAWISGSIIEKG[GOIMKB@DMJGLEB@@BB@B@@@B@@@DDBBB@BBB@BAB@B@B@@@BAB@@AB@B@@AB@@A@@@AAAAA@@AAA@A@@@@@C@CAA@@A@@A@CBE@DCDEDC@ABAFE@AB@@A@@AAAA@A@A@@CACCC@AA@@AA@@A@A@C@A@A@AAABECCAABAAA@A@AA@A@@AAA@E@@@AAA@@@A@@BA@@@@@A@@A@@A@@@A@C@AB@AA@@@@A@C@C@@AA@@@C@ABCBA@C@@@A@A@@BA@EB@AC@A@A@@@ABA@A@@@CCI@@@A@@BABCBA@@BABC@@@AAAA@CCCAA@A@C@A@@@AA@AC@@@AA@AA@AAA@A@C@E@ABA@ABA@AAA@@@@AAACC@@AA@AA@ECCACAA@A@C@@@AA@@@@B@DA@@DAFCBAB@@A@A@@@A@AB@@ABA@@A@@@C@AAC@C@CAC@A@@BA@C@G@E@C@ABA@CBE@EBEDCBCBIDCBA@@@C@AAA@@A@@@C@@@@AAA@A@@@AA@ACAE@C@A@ACAAA@AC@A@@A@@@CAC@@@AA@@AAA@C@A@A@A@ABABA@A@A@C@A@AA@A@@BAB@BC@AAAB@@AB@@A@@@ACA@AA@BA@ABA@@@@AAA@AACACAA@A@ICECAAA@C@AA@@@@@AEAAC@@AA@ABABE@@@@@EAA@@BA@@HAB@BAB@@A@G@@A@G@A@@AA@@CAAACAACCCACACA@@A@@@ADF@@BD@@BBB@@B@@BBD@@@B@@@@A@A@@@BD@B@BA@A@@AA@@AC@A@@AAB@@AF@@AB@@@@GAA@@@CAE@@EAA@@CCAAAA@AC@BA@@BCBC@@BA@@B@JA@@B@@@@@@A@@A@A@EAC@A@AA@@A@@@@DAD@BABABA@@DA@@@AB@A@@ABA@AA@@@A@@BA@AA@@@C@@AA@@A@@@AACAC@A@@BA@CBA@ABA@@@@@AC@AAA@A@C@@A@@A@AAA@@@@AB@DABAHAFAFABABBD@BBB@D@B@DAD@HCB@BCBA@CDABABAB@B@B@@A@@@@CCA@E@EA@@@@AACE@AA@@@A@@@IBEBCBC@C@K@C@E@CBE@A@C@CAABCAAC@@OOYOGIEIIE]E[CAAGI@M@QIKKKAAMGAAIKGIKKIIQOMMA@CICKBIDMDIFQJIDE@@AACAECAA@A@A@@C@AACAAAAAAAC@AAAAA@CAA@AAA@EE@A@A@@AAC@@@EE@A@@@ACA@AA@@AKEQBG@I@M@QHODGDGBEDA@C@A@@@@@@@A@A@C@A@@@@@@B@@BD@@@B@@@BABADBDAB@@BF@B@B@@B@@B@@@@CB@@@@@BEDEDEH@@B@HB@@@@IBAB@@@@@BB@BB@@FD@BBB@@@BB@B@DDBB@@@@EDABA@@@@B@@BD@@@@BB@AB@B@B@@@BB@@@@ABAB@BA@FA@@@B@BBBAFBD@@JBB@B@@B@B@@@B@B@@BBB@B@@BB@@BBB@@BB@@@BDB@@@@A@A@A@KAC@@@@@@BAB@B@@@@@B@@@@CAABA@@@C@@@ABABA@@@@BB@B@B@BB@@@BA@@@@BFBHB@@BBBB@DAH@B@BBF@@@@@@@@BB@DB@BD@@A@@@AB@@@B@BBBABAB@BAF@B@DAB@BB@@BFFDDBB@@BB@BABA@@@CC@A@A@@AA@@C@@@ECAAEAA@EAKA@AA@@A@@A@@@@@@@@@AB@D@H@BC@EJCJENALETELIDGFCBAD@BEH@F@BBJ@LALCHILMHKDABG@KDEDCDCFAFDDBDDLDJ@FAJAFCHBHALCLEFAFGFEFIDKDKDABCDBFDFBJALAFEHCDIBGBIFEDGFEHAFFJDFBFEJKBIBGHCD@F@FALENGJKLKHEBABIFMFEDCFAH@HAF@HDFBFCJCH@@CDAHBFBH@F@HHHJNFLHJ@DBHBL@BAJALAL@LAHEHEDI@K@IAI@C@Q@SAE@@@C@ABC@E@IB@@@@AA@CAAIAA@EDC@ABA@CAAAA@EA@@A@@BE@@@A@@B@@B@BB@@B@AB@@@@A@C@CAA@A@AB@@E@EAE@ICA@@BA@AB@@BB@@@D@BABA@@@ABE@ABABA@ABA@A@AAC@AAE@A@C@A@@@AB@@@BBFDB@B@@A@@B@@AB@@EAGAA@CAGCCAA@@@@BAFAB@@AAA@A@CDADABE@C@@BC@CBEFA@BDB@A@@@C@@@ADC@@@AAAAA@@@A@CD@BCAG@GAA@CBC@ABC@CAA@CAA@E@CBA@A@@@AB@B@B@@ABABABEF@B@@@@ABA@A@C@@@CDABAB@@A@ACA@ABA@@ACAA@C@@BABABAD@B@D@B@F@@@BADABAD@BABA@ABABC@@B@@B@DBBB@@@@A@CBC@EBA@C@E@E@@@@@@@A@C@A@AAA@A@ABAB@@@@@D@@@BA@@@@B@@@B@B@@EAAAIEIF@@@BBD@@BB@BB@KLCCAAAAAA@@CBA@@@@@@C@@@@EB@@A@@@@@@D@BAD@@C@C@GAGA@@A@AB@B@B@D@@BDDD@DB@BB@@AB@B@BB@BB@BFHB@FD@@BDDBDB@@@@@BCBAB@BAB@BBBD@DBB@F@B@BBDBDFAB@@DDFBAD@B@D@@BH@D@D@FBD@B@B@@CD@@@@BD@BA@ABA@GBA@E@C@CBC@ABA@ABA@C@A@A@ABAB@@A@AACCA@@@@@A@@@MLIDKFGFCFGFCBIBCDFFDPFDJDJJ@B@DBLFFD@JDBB@BDFHHHBDBL@B@H@LCH@FFBHDFBBCHBBHFBJBN@D@BB@@LCH@BADGXBLFFDFHJLDR@JB@@PFHAHDNRFFFHADFFRHHR@LNR@BBH@DBBBHHHAH@L@@HDJDTNPL\\RFJ@BDD@@TDHFPFRP@@THXPJNBD@VILEFSDWBGHW`_\\QVAXF^@@X^D@H@JDD@PJF@JBJ@HNJ@@DCD@FJDHCJGLAB@L@@B@@L`ADCB@DAD@FJH@DADAB@DBFAFBJ@@DBADFHLFHCH@DDF@HCDAPBFCFAHAFDDF@NEHAJIFAFCDEDE@GBADBDJBBB@BD@@B@AJBB@DCH@D@JEB@JBDBBBAJHH@HED@BA@GHBBDD@B@@FHCVLHL@TLCNEHLZAHFFDD@H@DFRH^dP^HTELC~Z`GB@rNRBD@Ā£D@B@D@DFPDDDDJHBF@DAD@@CACEEBEDCXHJDF@DADGDEJCH@DBDB@DEBGF@BDDD@H@L@PAL@LDTFHCHC`CP@FAD@FCHAB@@@\\BLJTLJJJFHXV@FDJDJBKRVLHLLDNIFEfPBLFJNLDBZmVe@AEC@Ug[uX]BA@AJI@AWM@@S]EOHE`QB@PMA@OG@EAA@@@A@@BA@APH@@BABQD]BANITODCTLkDEjw@CBEHaFM^mC@BENoBEHEJKBABAJMFKHSPOBO@@@@DCD@BABAB@BBB@@B@@@DABAB@B@@@B@@B@@@B@B@BAFABABABA@@BBB@@@BBAS@AKBA@A@C@AAA@@@AA@@@A@@@A@AB@D@TE@C@CBO@EBA@A@C@@A@AAA@@A@C@A@@@@FGBCBEHGEE@AhEJCJEDIDG@@GIAKLMNMPU\\SDAhYBUTSFEHBLCD@DAFAF@BIC@^QFBNKNGDAZK@@`KTIB@LELCAO@GAY@EQJAAAAAAC@AA@@A@ACC@@AAAACAAAAA@CB@BE@@FGNCr]JETKFIDA@ABABABC@@@ABC@ABADAD@BAFA@@@@@C@@BABAAAYMA@@AB@DAB@B@BADCDCBAB@@AB@BAF@B@NAF@DBFDDBBAHAA@@@BB@@"],"encodeOffsets":[[123788,43286]]}}],"UTF8Encoding":true});}));