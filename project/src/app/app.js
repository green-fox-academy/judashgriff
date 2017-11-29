var React = require('react');
var ReactDOM = require('react-dom');

// class Header extends React.Component {
//     render() {
//         return(
//             <h1>Hello world! df dkjhf </h1>
//         );
//     }
// };

class ShoppingList extends React.Component {
    render() {
      return (
        <div className="shopping-list">
          <h1>Shopping List for {this.props.name}</h1>
          <ul>
            <li>Kiskutya</li>
            <li>kaka</li>
            <li>Oculus</li>
          </ul>
        </div>
      );
    }
  }

ReactDOM.render(<ShoppingList name="Banderas" />, document.getElementById('todo-wrapper'))