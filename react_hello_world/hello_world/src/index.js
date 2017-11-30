import React from 'react';
import ReactDOM from 'react-dom';
import './style.scss';



class Hello extends React.Component {
    render() {
        return ( 
            <div class="container">
                <h1>Hello World</h1>
                <br/>
                <table>
                    {/* {table} */}
                    <p>Hy, I am the table placeholder! </p>
                </table>
            </div>
        );
    }
};



ReactDOM.render(
    <Hello />,
    document.querySelector('body')
);