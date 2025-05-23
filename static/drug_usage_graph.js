function make_graph(data) {

  data = eval(data)

  var svg = d3.select("#plot").attr("width", 640).attr("height", 640);

  var margin = {top: 10, right: 40, bottom: 60, left: 60},
  width = 450 - margin.left - margin.right,
  height = 400 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3.select("#plot")
    .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");

  // X scale and Axis
  var x = d3.scaleLinear()
    .domain([0, d3.max(d3.map(data, d=>d[0]))])
    .range([0, width]);
  svg
    .append('g')
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("y", -40)
    .attr("x", -60)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("Self help meetings attended");

  // Y scale and Axis
  var y = d3.scaleLinear()
    .domain([0, d3.max(d3.map(data, d=>d[1]))])
    .range([height, 0]);
  svg
    .append('g')
    .call(d3.axisLeft(y));
  
  svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", 2*width/3+40)
    .attr("y", height + 40)
    .text("Drug use effect on mental health");

  svg
    .selectAll("circles")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", function(d){ return x(d[0]) })
    .attr("cy", function(d){ return y(d[1]) })
    .attr('opacity', .05)
    .attr("r", 7)

}