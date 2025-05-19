var data = "{{data}}"

var svg = d3.select("#plot").attr("width", 640).attr("height", 640);

var margin = {top: 10, right: 40, bottom: 30, left: 30},
 width = 450 - margin.left - margin.right,
 height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svG = d3.select("#plot")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
     "translate(" + margin.left + "," + margin.top + ")");

// X scale and Axis
var x = d3.scaleLinear()
  .domain([0, 10])
  .range([0, width]);
svG
  .append('g')
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

// Y scale and Axis
var y = d3.scaleLinear()
  .domain([-10, 10])
  .range([height, 0]);
svG
  .append('g')
  .call(d3.axisLeft(y));

svG
  .selectAll("circles")
  .data(data)
  .enter()
  .append("circle")
  .attr("cx", function(d){ return x(d[0]) })
  .attr("cy", function(d){ return y(d[1]) })
  .attr("r", 7)