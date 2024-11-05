import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';
import {Provider} from "react-redux";
import configureStore from 'redux-mock-store';

const mockStore = configureStore([]);
const store = mockStore({
    background: {
        fireflies: []
    }
});


test('renders learn react link', () => {
  render(
      <Provider store={store}>
          <App />
      </Provider>
  );
  const linkElement = screen.getByText(/Documentation de l'API/i);
  expect(linkElement).toBeInTheDocument();
});