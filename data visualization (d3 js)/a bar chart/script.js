d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json")
  .then(function (data) {
    const dataset = data.data;

    const margin = { top: 20, right: 30, bottom: 60, left: 60 },
      width = 800 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

    const svg = d3
      .select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    dataset.forEach((d) => {
      d[1] = +d[1];
      d[0] = new Date(d[0]);
    });

    const x = d3
      .scaleTime()
      .range([0, width])
      .domain(d3.extent(dataset, (d) => d[0]));

    const y = d3
      .scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(dataset, (d) => d[1])]);

    const xAxis = d3.axisBottom(x).ticks(d3.timeYear.every(5)).tickFormat(d3.timeFormat("%Y"));

    svg
      .append("g")
      .attr("id", "x-axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")
      .style("text-anchor", "middle")
      .attr("dx", "0em")
      .attr("dy", "1em")
      .attr("transform", "rotate(0)");

    svg.append("g").attr("id", "y-axis").call(d3.axisLeft(y));

    function getQuarter(date) {
      const month = date.getMonth() + 1; // getMonth() returns month from 0 to 11
      if (month <= 3) return "Q1";
      else if (month <= 6) return "Q2";
      else if (month <= 9) return "Q3";
      else return "Q4";
    }
    svg
      .selectAll(".bar")
      .data(dataset)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", (d) => x(d[0]))
      .attr("width", width / dataset.length)
      .attr("y", (d) => y(d[1]))
      .attr("height", (d) => height - y(d[1]))
      .attr("data-date", (d) => d[0].toISOString().substring(0, 10))
      .attr("data-gdp", (d) => d[1])
      .on("mouseover", function (event, d) {
        const date = d[0];
        const quarter = getQuarter(date);
        const year = date.getFullYear();
        const formattedGDP = d[1].toLocaleString();
        tooltip.transition().duration(200).style("opacity", 0.9);
        tooltip
          .html(`${year} ${quarter} <br/> \$${formattedGDP} Billion`)
          .attr("data-date", d[0].toISOString().substring(0, 10))
          .style("left", event.pageX + 5 + "px")
          .style("top", event.pageY - 28 + "px");
      })

      .on("mouseout", function (d) {
        tooltip.transition().duration(500).style("opacity", 0);
      });

    const tooltip = d3.select("body").append("div").attr("id", "tooltip").style("opacity", 0);

    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", 0 - margin.top / 2)
      .attr("text-anchor", "middle")
      .style("font-size", "24px")
      .style("text-decoration", "underline")
      .text("United States GDP");

    svg
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - height / 2)
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Gross Domestic Product");

    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", height + margin.bottom)
      .attr("text-anchor", "middle")
      .style("font-size", "12px")
      .text("More Information: http://www.bea.gov/national/pdf/nipaguid.pdf"); // Add title
    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", 0 - margin.top / 2)
      .attr("text-anchor", "middle")
      .style("font-size", "24px")
      .style("text-decoration", "underline")
      .text("United States GDP");

    svg
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - height / 2)
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Gross Domestic Product");

    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", height + margin.bottom)
      .attr("text-anchor", "middle")
      .style("font-size", "12px")
      .text("More Information: http://www.bea.gov/national/pdf/nipaguid.pdf");
  })
  .catch(function (error) {
    console.error("Error loading or parsing data:", error);
  });
