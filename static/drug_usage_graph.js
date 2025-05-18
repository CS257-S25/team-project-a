require('d3@v6')

svgWidth = 640
svgHeight = 640

margin = {
  return: {
    top: 10,
    right: 10,
    bottom: 20,
    left: 20
  }
};


var data = [ {x:10, y:20}, {x:40, y:90}, {x:80, y:50} ]

xScale_m = d3.scaleLinear()
  .domain(d3.extent(data, d=>d.x))
  .range([margin.left, svgWidth - margin.right])

yScale_m = d3.scaleLinear()
  .domain(d3.extent(data, d=>d.y))
  .range([svgHeight - margin.bottom, margin.top])

let svg = d3.create('svg').attr('height', svgHeight).attr('width', svgWidth);
  
svg.selectAll('circle')
    .data(data)
    .join('circle')
    .attr('cx', d => xScale(d.x))
    .attr('cy', d => svgHeight-yScale(d.y))
    .attr('r', d => 5)
    .attr('fill', color)

svg.append('g')
    .attr('transform', `translate(0, ${svgHeight - margin.bottom})`)
    .call(d3.axisBottom(xScale_m));
  
svg.append('g')
    .attr('transform', `translate(${margin.left}, 0)`)
    .call(d3.axisLeft(yScale_m));

return svg
