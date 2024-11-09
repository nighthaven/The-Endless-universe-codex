import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import BackgroundComponent from './background.component';

const mockStore = configureStore();
const store = mockStore({
  background: {
    fireflies: [],
  },
});

test('background component render', () => {
  render(
    <Provider store={store}>
      <BrowserRouter>
        <BackgroundComponent />
      </BrowserRouter>
    </Provider>
  );
  const backgroundElement = screen.getByTestId('background');
  expect(backgroundElement).toBeInTheDocument();
});
