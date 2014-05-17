function d2h(d) {
  return d.toString(16);
}

function h2d (h) {
  return parseInt(h, 16);
}

String.prototype.toHex = function() {
  var tmp = this,
      str = '',
      i = 0,
      tmp_len = tmp.length,
      c;

  for (; i < tmp_len; i += 1) {
    c = tmp.charCodeAt(i);
    var x = d2h(c);
    str += d2h(c);
  }
  return str;
}

String.prototype.hexToString = function() {
  var tmp = this,
      arr = tmp.split(' '),
      str = '',
      i = 0,
      arr_len = arr.length,
      c;

  for (; i < arr_len; i += 1) {
    c = String.fromCharCode( h2d( arr[i] ) );
    str += c;
  }

  return str;
}
