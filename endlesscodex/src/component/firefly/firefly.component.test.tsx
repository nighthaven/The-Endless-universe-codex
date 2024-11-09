import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import FireflyComponent from './firefly.component';

const mockStore = configureStore();
const store = mockStore({
  background: {
    fireflies: [
      {
        id: 1,
        top: '50%',
        left: '50%',
        animationDuration: '5s',
      },
    ],
  },
});

test('firefly render', () => {
  render(
    <Provider store={store}>
      <FireflyComponent />
    </Provider>
  );
  const fireflyElement = screen.getByTestId('firefly');
  expect(fireflyElement).toBeInTheDocument();
});
