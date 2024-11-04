import type { Config } from '@jest/types';

const config: Config.InitialOptions = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  transform: {
    '^.+\\.tsx?$': 'ts-jest',
    '^.+\\.jsx?$': 'babel-jest',
  },
  moduleNameMapper: {
    '\\.(jpg|jpeg|png|gif|webp|svg)$': '<rootDir>/src/__mocks__/fileMock.ts',
    '\\.(css|scss)$': 'identity-obj-proxy',
  },
  transformIgnorePatterns: [
    '/node_modules/(?!axios)'
  ],
  setupFilesAfterEnv: ['<rootDir>/src/setupTests.ts'],
};

export default config;