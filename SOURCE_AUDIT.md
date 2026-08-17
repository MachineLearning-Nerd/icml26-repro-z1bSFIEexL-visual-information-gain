# Source audit

## Pinned paper artifacts

| Artifact | Path | SHA-256 |
| --- | --- | --- |
| arXiv PDF, version 2 | evidence/source/arxiv.pdf | b8c6f6c186b5dafc0236e86febf9ed4e71ece2b599d6cfe85df888c53f401a3 |
| arXiv source archive, version 2 | evidence/source/arxiv_source.tar.gz | 3302d743c3f3654aed8b78448f1bdb20c58d59b465253c43272ec28514c1c517 |

The checksum file at evidence/source/SHA256SUMS is checked by verify_final.py. The archive contains 45 members: 44 regular files and one directory, with no symlinks and no executable regular files. The source entry point is main.tex.

## Archive member inventory

The following hashes are computed over the uncompressed contents of each regular archive member.

~~~text
+d1f6b1a71c9accb812ec5121d1fff7910c025ca7bb201948bacdb40941bc14e5  00README.json
48d18794a5d97c0479a588cc2eac0917992feb9da83acc4631b8f55757d80f9b  algorithmic.sty
93fd0eb31c112eb405833db8f1d7f5d238c7e691b1c05680d7276e68f36d564a  algorithm.sty
f708ddd3555596e6680b366e1829b3a52d9353114754c729776eccf4aa2e49f7  example_paper.bib
9130c52f91087abc6d223164ffa587e207e3257fcbcd069ef09ecb5391043f14  fancyhdr.sty
e439b900940bc3e3b9d4256d00f91a293b07ae165c65fdfb3da3c1af82d999a0  fig/tab-sample2-2.png
9371c3821c27bdb28fcecab65d391eb3e3dadcb2ba0f93306e053649f541257a  fig/tab-sample2-3.png
6327cb7b4e426532015c952d4665207b61ec6d0c99ae068adf8f61285ff0555d  fig/tab-sample2-1.png
eb47bcd24bc7cd0d6a0afd33db57c4f689aa43d23108065ab49d45c3e75f1e8e  fig/fig-rel-sample.pdf
d8a372440489630c9c7b3627a3bcb55c9a819344b0ba607d53a757e025f3f799  fig/tab-sample4-2.png
33e8490fd1ed8ee795c181a89dc4ce50547653414e5169cf8c4b75b0f07e5051  fig/fig-vig-benchmark-box.pdf
7eadcc094cd232bc5430314b2efdb5b243ed6784cf5ea9a1f8090a619e817da6  fig/tab-sample4-3.png
d7399ae470c11b20ec612c133573f5b4d988c1287f81197db694660686ac3781  fig/fig-irrel-sample.pdf
af457d9c8d4b3cd651239566d9f3cf4c403991ba7520c7a5737cf6c6945e78a7  fig/tab-sample4-1.png
0dae3dd6c30feb99f0e01224f4abcaa1d2b4c7b81966671e8bdcc296a0232d00  fig/tab-sample1-3.png
a6f8d93aae5da704bbb512d8213e25bd254a4fee124f8a824551b4cf8c2900cd  fig/tab-sample3-1.png
ffb3d166f79c0034621779ffeaa915c7d53760f34e76f8f7144718c775953271  fig/fig-blind-bar-llava7b.pdf
c9280af950f9af26050d27b13afc804ab570f3a03fcbf1bdcdc533fa295d33a9  fig/fig-loss-diff-scatter.png
4ceb022dafd4c61a5bf772bf898fe2e8f0dc8d0361ed58639019c13b04b46e2e  fig/tab-sample1-2.png
988addbe495cae31da0b7acebd21806271fd9d8623eb24395449531b3635bb23  fig/tab-sample3-2.png
d08f50ea160e78b6828a149184484d82e694946c1abb6020229496d63a22d8c5  fig/fig-blind-bar-share4v.pdf
e5ee7cdbe562278c0a9017d142067a9f4c893c2f93f64031f3c9b3d6cacbb8a7  fig/fig-blur.jpg
204dc0b4c2b8928381712ba8d327c28e603eb2f0b523455e580a7361a04eca9c  fig/tab-sample3-3.png
eb60fef191e4f1454702c5ff1f5d47e76cc8eab47df9f7fd494e815aa86fda8d  fig/tab-sample1-1.png
b7daa5003e3dfcd5884bb66b98c8fff5296088e8bb5a61d3a07ee87d9957742c  fig/fig-var-line-share4v.pdf
98d606f5b986bd33a77933c68229429a0cd9b93ca39948e9d033c64efbd7e2ad  fig/tab-sample5-1.png
1123b12fc8ebc2daea6d1c1b4b9c25489757e180e46624b83b3e1fdf32fcfc57  fig/tab-vig-cat.png
0dd5ff49bb7c91360cbdc8fa45bd8d8216f2916ea30dae1d093ee75c2b073a8f  fig/fig-ratio-bar.pdf
6103bba1c73a9e9f18a18597ea71592a6c2a1c6d3df8312fc8a4ccf69f14eb8f  fig/fig-var-line-llava7b.pdf
08aaf636629703dca072470d96536a90e500ea5b10b29aa1bf88656bdf6be25f  fig/tab-sample5-2.png
e88de11a5caa8278536983909062b08714be9278d8d2a56d6ef3dc3eb0c7d139  fig/tab-sample5-3.png
e2599c4b1427b4695bf8ea6dbcb024603bc99339a9c651d2ae227033654e6742  fig/fig-long-tail-task.pdf
f355810e3a6c66b0ad12f0aeb076fd12c0f5e269b97947402c662d58cb6fad91  fig/fig-blind-bar-llava13b.pdf
15a510944b7d99ba0d842f2457a558090796508d39d57fc46553c225ea15b630  fig/fig-original.jpg
54a272a135de59bcd38679e6873c2b9bbe20cea9b3b6c1be9b1e214487ae4d4c  fig/tab-response-exp2.jpg
dcce6983503d3399a19858b3887ef5b5fb399f2c8a4b2c348bd99665df734fa7  fig/tab-response-exp1.jpg
098243f35c54bfc4074df6f80e5c16a1e6de8fa36ef5dbba882b944d23ed3e14  fig/fig-vig-pos.pdf
be99ff2c1ab3090191980ad144e4d69c6fc159820cfd7147e20fa69f750922cd  fig/tab-vig-cat2.png
16a01ac3a48b3f1bf0a8576e47e5f04dc753103e8facc95e7957078f69825ea8  fig/fig-var-line-llava13b.pdf
97d1a446d79c3f52c3c425a3f45977daecd4e52fbf2694e3b80175870a03df05  fig/tab-vig-dog.png
df6299af80944e77af8f254149e3cf5f46b291ac93f2e3a08f0d80f8fbb9df90  fig/fig-long-tail-object.pdf
0ec3d5eb9b02efb7e0b44a32f3775882f42a743d0bdc618f34e6936309b98764  icml2026.bst
7cdcf90f6a59c5219e7f15c88f7ed09fcaf598dad91e6cdddc4dc3cb0e397a95  icml2026.sty
e06490728ee80d279bf960fece950d9ce106909eef42aec64c6d6f468c941e20  main.tex
~~~

## Audit interpretation

The archive is a source record, not an implementation artifact. It contains the paper manuscript, figures, bibliography, and style files, but no runnable LVLM training pipeline, checkpoint, dataset, or independent benchmark output. Accordingly, its contents support source traceability and claim interpretation, not full-paper reproduction.
