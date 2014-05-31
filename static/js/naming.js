var namingify = function(name) {
  var now = new Date();

  name += now.toGMTString();

  var ENV = ['용기', '교만', '시기', '분노', '나태', '탐욕', '식탐', '색욕',
             '사랑', '증오', '졸림', '기쁨', '환호', '우울', '빡침' ],
      hexed = name.toHex().split(''),
      n = hexed,
      my_env = [];

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
    console.log(n[i]);
    var env = ENV[h2d(n[i])];
    if(my_env.indexOf(env) === -1) {
      my_env.push(env);
    }
  }

  var result = [];
  for(var i=0; i < my_env.length; i++) {
    result.push({
      'feel': my_env[i],
      'prob': prob[i]
    });
  }

  return result;
}
