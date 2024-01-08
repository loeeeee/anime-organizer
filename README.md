# Anime Series Organizer

It scans a media folder, and create symbolic links in another place with organized folder structure that can be processed by JellyFin server. It works on Linux. And the expected input folder structure is from VCB studio. However, other folder structure should also works fine, because of the ARTIFICIAL INTELLIGENCE of regular expression.

## How to use

The entry point is entry_point.py. 

## Example

### Source

test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/
├── CDs
│   ├── [230106] ORIGINAL SOUNDTRACK [24bit_48kHz] (flac)
│   │   ├── 01. お兄ちゃんはおしまい!.flac
│   │   ├── 02. 変な感じがする朝.flac
│   │   ├── 03. 落ち着け、、.flac
│   │   ├── 04. 何.flac
│   │   ├── 05. 困ったぞ.flac
│   │   ├── 06. サスペンスホラー.flac
│   │   ├── 07. 堪能してやろう.flac
│   │   ├── 08. 経過観察.flac
│   │   ├── 09. ショック.flac
│   │   ├── 10. アイキャッチA.flac
│   │   ├── 11. ボス戦.flac
│   │   ├── 12. アイキャッチB.flac
│   │   ├── 13. 着せ替え遊び.flac
│   │   ├── 14. 芽生える乙女心.flac
│   │   ├── 15. アイキャッチC.flac
│   │   ├── 16. BLゲーム.flac
│   │   ├── 17. 浮かれピンチ.flac
│   │   ├── 18. はじめてのスポブラ.flac
│   │   ├── 19. 楽しみな調理実習.flac
│   │   ├── 20. 懐かしい思い出.flac
│   │   ├── 21. ちょっと一息.flac
│   │   ├── 22. 爽やかな日々.flac
│   │   ├── 23. 悪くないかも.flac
│   │   ├── 24. 意気揚々!!.flac
│   │   ├── 25. 押し問答.flac
│   │   ├── 26. うずうず.flac
│   │   ├── 27. お兄ちゃんはおしまい! オルゴールVer..flac
│   │   ├── 28. ほのぼの.flac
│   │   ├── 29. まひろによる考察.flac
│   │   ├── 30. 神様、みはり様.flac
│   │   ├── 31. バトルオブクローンズ 俺大戦Ⅶ.flac
│   │   ├── 32. 散策.flac
│   │   ├── 33. レクリエーション.flac
│   │   ├── 34. ガールズトーク.flac
│   │   ├── 35. スペース☆タイタニック.flac
│   │   ├── 36. だらだらした時間.flac
│   │   ├── 37. 劣等感.flac
│   │   ├── 38. 魔法少女ニコララ.flac
│   │   ├── 39. ニコララ・スマイルハリケーン.flac
│   │   ├── 40. ハピネス・フルフィルド.flac
│   │   ├── 41. たわむれ.flac
│   │   ├── 42. ほっと一息.flac
│   │   ├── 43. キラキラしている.flac
│   │   ├── 44. トキメキ.flac
│   │   ├── 45. スーパーマーケット.flac
│   │   ├── 46. わちゃわちゃと.flac
│   │   ├── 47. 忘れてた.flac
│   │   ├── 48. サイエンサー.flac
│   │   ├── 49. 我慢の限界.flac
│   │   ├── 50. 補習が待っている.flac
│   │   ├── 51. 枕投げ.flac
│   │   ├── 52. 前向き.flac
│   │   ├── 53. ロスクエの話!.flac
│   │   ├── 54. アイキャッチ ロスクエVer..flac
│   │   ├── 55. Twincle Dancer.flac
│   │   ├── 56. エロゲー.flac
│   │   ├── 57. 頑張る姿.flac
│   │   ├── 58. タロット占い A.flac
│   │   ├── 59. タロット占い B.flac
│   │   ├── 60. イルミネーション.flac
│   │   ├── 61. お正月.flac
│   │   ├── 62. 旅館.flac
│   │   └── 63. 冬景色.flac
│   ├── [230215] ｢ひめごと＊クライシスターズ｣／ONIMAI SISTERS (flac+webp)
│   │   ├── 01. ひめごと＊クライシスターズ.flac
│   │   ├── 02. ひめごと＊クライシスターズ(TV size ver.).flac
│   │   ├── 03. ひめごと＊クライシスターズ(まひろver.).flac
│   │   ├── 04. ひめごと＊クライシスターズ(みはりver.).flac
│   │   ├── 05. ひめごと＊クライシスターズ(かえでver.).flac
│   │   ├── 06. ひめごと＊クライシスターズ(もみじver.).flac
│   │   ├── 07. ひめごと＊クライシスターズ(Instrumental).flac
│   │   ├── PCCG-02194.log
│   │   └── Scans
│   │       ├── 01.webp
│   │       ├── 02.webp
│   │       ├── 03.webp
│   │       ├── 04.webp
│   │       ├── 05.webp
│   │       ├── 06.webp
│   │       ├── 07.webp
│   │       ├── 08.webp
│   │       └── 09.webp
│   ├── [230215] ｢ひめごと＊クライシスターズ｣／ONIMAI SISTERS [24bit_48kHz] (flac)
│   │   ├── 01. ひめごと＊クライシスターズ.flac
│   │   ├── 02. ひめごと＊クライシスターズ (TV Size Ver.).flac
│   │   ├── 03. ひめごと＊クライシスターズ (まひろ Ver.).flac
│   │   ├── 04. ひめごと＊クライシスターズ (みはり Ver.).flac
│   │   ├── 05. ひめごと＊クライシスターズ (かえで Ver.).flac
│   │   ├── 06. ひめごと＊クライシスターズ (もみじ Ver.).flac
│   │   └── 07. ひめごと＊クライシスターズ (Instrumental).flac
│   ├── [230215] ｢アイデン貞貞メルトダウン｣／えなこ feat. P丸様。 (flac+webp)
│   │   ├── 01. アイデン貞貞メルトダウン.flac
│   │   ├── 02. アイデン貞貞メルトダウン(TV size).flac
│   │   ├── 03. アイデン貞貞メルトダウン(えなこパートver.).flac
│   │   ├── 04. アイデン貞貞メルトダウン(P丸様。パートver.).flac
│   │   ├── 05. アイデン貞貞メルトダウン(Instrumental).flac
│   │   ├── PCCG-02195-1.log
│   │   └── Scans
│   │       ├── 01.webp
│   │       ├── 02.webp
│   │       ├── 03.webp
│   │       ├── 04.webp
│   │       ├── 05.webp
│   │       ├── 06.webp
│   │       ├── 07.webp
│   │       └── 08.webp
│   └── [230215] ｢アイデン貞貞メルトダウン｣／えなこ feat. P丸様。 [24bit_48kHz] (flac)
│       ├── 01. アイデン貞貞メルトダウン.flac
│       ├── 02. アイデン貞貞メルトダウン (TV Size).flac
│       ├── 03. アイデン貞貞メルトダウン (えなこパートver.).flac
│       ├── 04. アイデン貞貞メルトダウン (P丸様。パートver.).flac
│       └── 05. アイデン貞貞メルトダウン (Instrumental).flac
├── SPs
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [CM_15s][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [CM_30s][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [CM_Blu-ray][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Eyecatch EP01-06][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Eyecatch EP07-12][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Menu01][Ma10p_1080p][x265_flac].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Menu02][Ma10p_1080p][x265_flac].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [NCED][Ma10p_1080p][x265_flac].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [NCOP][Ma10p_1080p][x265_flac].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [PV01][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [PV02][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [TVSP][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 02][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 03][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 04][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 05][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 06][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 07][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 08][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 09][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 10][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 11][Ma10p_1080p][x265_ac3].mkv
│   ├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview 12][Ma10p_1080p][x265_ac3].mkv
│   └── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Web Preview Epilogue][Ma10p_1080p][x265_ac3].mkv
├── Scans
│   ├── Vol.1
│   │   ├── 01-01.webp
│   │   ├── 01-02.webp
│   │   ├── 01-03.webp
│   │   ├── 01-04.webp
│   │   ├── 01-05.webp
│   │   ├── 01-06.webp
│   │   ├── 02-01.webp
│   │   ├── 03-01.webp
│   │   ├── 03-02.webp
│   │   ├── 03-03.webp
│   │   ├── 03-04.webp
│   │   ├── 04-01.webp
│   │   ├── 04-02.webp
│   │   ├── 04-03.webp
│   │   ├── 05-01.webp
│   │   ├── 06-01.webp
│   │   ├── 07-01.webp
│   │   ├── 07-02.webp
│   │   ├── 08-01.webp
│   │   ├── 08-02.webp
│   │   └── 09-01.webp
│   └── Vol.2
│       ├── 01-01.webp
│       ├── 01-02.webp
│       ├── 01-03.webp
│       ├── 01-04.webp
│       ├── 01-05.webp
│       ├── 01-06.webp
│       ├── 02-01.webp
│       ├── 03-01.webp
│       ├── 03-02.webp
│       ├── 03-03.webp
│       ├── 03-04.webp
│       ├── 04-01.webp
│       ├── 04-02.webp
│       ├── 04-03.webp
│       ├── 05-01.webp
│       ├── 07-01.webp
│       ├── 07-02.webp
│       ├── 08-01.webp
│       └── 08-02.webp
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [01][Ma10p_1080p][x265_flac_2ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [01][Ma10p_1080p][x265_flac_2ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [01][Ma10p_1080p][x265_flac_2ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [02][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [02][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [02][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [03][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [03][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [03][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [04][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [04][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [04][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [05][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [05][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [05][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [06][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [06][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [06][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [07][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [07][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [07][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [08][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [08][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [08][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [09][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [09][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [09][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [10][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [10][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [10][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [11][Ma10p_1080p][x265_flac_ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [11][Ma10p_1080p][x265_flac_ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [11][Ma10p_1080p][x265_flac_ac3].mkv
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [12][Ma10p_1080p][x265_flac_2ac3].chs.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [12][Ma10p_1080p][x265_flac_2ac3].cht.ass
├── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [12][Ma10p_1080p][x265_flac_2ac3].mkv
└── [SweetSub&VCB-Studio] Oniichan ha Oshimai! [Fonts].7z

### Target

test/target/Oniichan_Ha_Oshimai!/
└── Season_1
    ├── S01E01.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [01][Ma10p_1080p][x265_flac_2ac3].chs.ass
    ├── S01E01.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [01][Ma10p_1080p][x265_flac_2ac3].mkv
    ├── S01E02.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [02][Ma10p_1080p][x265_flac_ac3].cht.ass
    ├── S01E02.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [02][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E03.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [03][Ma10p_1080p][x265_flac_ac3].cht.ass
    ├── S01E03.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [03][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E04.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [04][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E04.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [04][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E05.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [05][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E05.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [05][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E06.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [06][Ma10p_1080p][x265_flac_ac3].cht.ass
    ├── S01E06.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [06][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E07.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [07][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E07.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [07][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E08.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [08][Ma10p_1080p][x265_flac_ac3].cht.ass
    ├── S01E08.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [08][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E09.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [09][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E09.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [09][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E10.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [10][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E10.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [10][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E11.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [11][Ma10p_1080p][x265_flac_ac3].chs.ass
    ├── S01E11.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [11][Ma10p_1080p][x265_flac_ac3].mkv
    ├── S01E12.chi.ass -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [12][Ma10p_1080p][x265_flac_2ac3].cht.ass
    └── S01E12.mkv -> /home/foo/Projects/anime-organizer/test/mimic/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [Ma10p_1080p]/[SweetSub&VCB-Studio] Oniichan ha Oshimai! [12][Ma10p_1080p][x265_flac_2ac3].mkv
