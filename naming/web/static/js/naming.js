String.prototype.namingify = function() {

  var ENV = ['용기', '교만', '시기', '분노', '나태', '탐욕', '식탐', '색욕',
             '사랑', '증오', '졸림', '기쁨', '환호', '우울', '빡침' ],
      name = this,
      hexed = name.toHex().split(''),
      n = [];
  for(var i=0; i < hexed.length; i++) {
    n.push(hexed[i]);
    n.push(hexed[(hexed.length - 1) - i]);
  }

  var qu = Math.floor(n.length / ENV.length),
      prob = [];

  for(var i=0; i < n.length; i += qu) {
    prob.push(n.slice(i, i + qu));
  }

  console.log(prob);

  return n;
}
