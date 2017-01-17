var nodeIds, nodesArray, nodes, edgesArray, edges, network;

function startNetwork() {
    // create an array with nodes
    nodesArray = [
        {id: 0, label: 'localhost', group: 'localhost', fixed: true}
    ];
    nodes = new vis.DataSet(nodesArray);

    // create an array with edges
    edgesArray = [
    ];
    edges = new vis.DataSet(edgesArray);

    // create a network
    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };

    // http://html-color-codes.info/webfarben_hexcodes/
    var options = {
        groups: {
          'localhost': {
            shape: 'square',
            color: "#848484"
          },
          'hosts': {
            shape: 'dot',
            color: "#0040FF"
          },
          'services': {
            shape: 'triangle',
            color: "#3ADF00"
          }
        }
    }

    network = new vis.Network(container, data, options);

    network.on("click", function (params) {
        graphViewObject.clickedOnNode(params.nodes);
    });
}

function addNode(parent_id_, id_, label_, group_) {
    nodes.add({id: id_, label: label_, group: group_});
    edges.add({from: parent_id_, to: id_});
}

startNetwork();