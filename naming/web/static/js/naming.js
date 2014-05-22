var namingify = function(name) {
  var now = new Date();

  name += now.toGMTString();

  var ENV = ['용기', '교만', '시기', '분노', '나태', '탐욕', '식탐', '색욕',
             '사랑', '증오', '졸림', '기쁨', '환호', '우울', '빡침' ],
      hexed = name.toHex().split(''),
      n = [],
      my_env = [];
  for(var i=0; i < hexed.length; i++) {
    n.push(hexed[i]);
    n.push(hexed[(hexed.length - 1) - i]);
  }

  var nl = 5 - h2d(n[0]) % 3,
      l = Math.floor(n.length / nl),
      prob = [];

  for(var i=0; i < n.length; i += l) {
    prob.push(h2d(n.slice(i, i + l).join('')));
  }

  sum = 0;
  prob.map(function(item, i) {
    sum += item;
  });

  prob.map(function(item, i) {
    prob[i] = prob[i] / sum;
  });

  for(var i=0; i < nl; i++) {
    my_env.push(ENV[h2d(n[i])]);
  }

  var result = [];
  for(var i=0; i < nl; i++) {
    result.push({
      'feel': my_env[i],
      'prob': prob[i]
    });
  }

  return result;
}
