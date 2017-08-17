import React from 'react';
import ReactDOM from 'react-dom';
import Picker from './components/picker';
import TriggerEffect from './components/trigger_effect';
import TestButton from './components/test_button';
import ClearButton from './components/clear_button';

class Brazier extends React.Component {
    render() {
        return (
            <div>
                <section>
                    <div>
                        <ClearButton />
                    </div>
                    <div>
                        <TestButton />
                    </div>
                    <ul>
                        <li>
                            <TriggerEffect label="Candle" effect="candle" />
                        </li>
                    </ul>
                </section>
                <section>
                    <Picker initialColor="rgb(0,0,0,1)" />
                </section>
            </div>
        )
    }
}

ReactDOM.render(<Brazier />, document.getElementById('app'));
