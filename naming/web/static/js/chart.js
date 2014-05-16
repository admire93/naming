var draw_pie_feel = function(args) {

      var width = 500;

      var radius = width / 2;

      var color = function(d) {
        var c = ["#468966", "#FFF0A5", "#FFB03B", "#B64926", "#8E2800"];
        var idx = 0;
        for(i in args) {
          if(d.data['feel'] == args[i]['feel']) {
            idx = i;
          }
        }
        return c[idx % c.length];
      }

      var pie = d3.layout.pie()
          .sort(null)
          .value(function(d) { return d['prob']; });

      var arc = d3.svg.arc()
          .outerRadius(radius - 10)
          .innerRadius(150);

      var svg = d3.select('#result').append('svg')
          .attr('width', width)
          .attr('height', width)
        .append('g')
          .attr('transform', 'translate(' + width / 2 + ',' + width / 2 + ')');

      var g = svg.selectAll(".arc")
          .data(pie(args))
        .enter().append("g")
          .attr("class", "arc");

       g.append("path")
       .attr("d", arc)
       .style("fill", function(d) { return color(d); });

       g.append("text")
       .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
       .attr("dy", ".35em")
       .style("text-anchor", "middle")
       .text(function(d) { return d.data['feel']; });
}
