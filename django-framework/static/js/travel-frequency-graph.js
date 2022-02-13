$(document).ready( function(){
    //svg which is the background picture for the graph

    var svg = d3.select("svg"),
        margin = 200,
        width = svg.attr("width") - margin,
        height = svg.attr("height") - margin;
    //define the scale for x and y

    var xScale = d3.scaleTime().range ([0, width]),
        yScale = d3.scaleLinear().range ([height, 0]);



    //domain of x and y scale
    var minDate = new Date(d3.min(data, function(d) { return d.date; }));
    minDate.setDate(minDate.getDate()-1);
    var maxDate = new Date(d3.max(data, function(d) { return d.date; }));
    maxDate.setDate(maxDate.getDate()+1);


    xScale.domain([minDate, maxDate]);
    yScale.domain([0, d3.max(data, function (d) {
        return d.frequency;})]);

    //grouping graph attributes
        var g = svg.append("g")
                   .attr("transform", "translate(" + 100 + "," + 100 + ")");

    //define x axies detail
        g.append("g")
         .attr("transform", "translate(0," + height + ")")
         .call(d3.axisBottom(xScale));
    //define y axies detail
        g.append("g")
         .call(d3.axisLeft(yScale).tickFormat(function(d){
             return  d+"Times";
         }).ticks(5))
            //label start
         .append("text")
         .attr("y", -50)
         .attr("dy",".71em")
         .attr("text-anchor", "end")
         .attr("stroke", "black")
         .text("Frequency");


    //drawing bar in the graph
    svg.selectAll()
    .data(data)
    .enter().append("rect")
    .attr("transform", "translate(" + 100 + "," + 100 + ")")
    .attr("class", "bar")
    .attr("x", function (d) {
    return xScale(d.date);
})
    .attr("width", width/15)
    .attr("y", function (d) {
    return yScale(d.frequency);
})
    .attr("height", function (d) {
    return height-yScale(d.frequency);



});
})