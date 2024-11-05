import React from 'react';
import { render, screen } from '@testing-library/react';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom'; // Importe BrowserRouter
import configureStore, { MockStoreEnhanced } from 'redux-mock-store';
import BackgroundComponent from './background.component';


type RootState = {
    background: {
        fireflies: Array<any>;
    };
};


const mockStore = configureStore<RootState>([]);

describe('BackgroundComponent', () => {
    let store: MockStoreEnhanced<RootState>;

    beforeEach(() => {

        store = mockStore({
            background: { fireflies: [] },
        });
    });

    test('renders the background component with children', () => {
        render(
            <Provider store={store}>
                <BrowserRouter>
                    <BackgroundComponent>Test Content</BackgroundComponent>
                </BrowserRouter>
            </Provider>
        );

        const contentElement = screen.getByText(/Test Content/i);
        expect(contentElement).toBeInTheDocument();
    });
});
