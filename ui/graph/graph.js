var nodeIds, nodesArray, nodes, edgesArray, edges, network;

function startNetwork() {
    // create an array with nodes
    nodesArray = [
        {id: 1, label: 'localhost', group: 'localhost', fixed: true}
    ];
    nodes = new vis.DataSet(nodesArray);

    // create an array with edges
    edgesArray = [
        //{from: 1, to: 3}
    ];
    edges = new vis.DataSet(edgesArray);

    // create a network
    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };

    var options = {
        groups: {
          'localhost': {
            shape: 'square',
            color: "#2B7CE9" // blue
          },
          'hosts': {
            shape: 'dot',
            color: "#109618" // green
          }
        }
    }

    network = new vis.Network(container, data, options);

    network.on("click", function (params) {
        params.event = "[original event]";
        graphViewObject.clickedOnNode(JSON.stringify(params, null, 4));
    });
}

function addNode(label_) {
    var newId = (Math.random() * 1e7).toString(32);
    nodes.add({id:newId, label:label_, group: 'hosts'});
    edges.add({from: 1, to: newId});
}

startNetwork();