'use client';

import { motion } from 'framer-motion';
import clsx from 'clsx';
import { ReactNode, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../store/store';
import {
  showItem,
  hideItem,
} from '../../store/item-layout/item-layout.reducer';

interface ItemLayoutProps {
  children: ReactNode;
  /* eslint-disable react/require-default-props */
  className?: string;
}

function ItemLayoutComponent({ children, className }: ItemLayoutProps) {
  const dispatch = useDispatch();
  const isVisible = useSelector((state: RootState) => state.item.visible);

  useEffect(() => {
    dispatch(showItem());

    return () => {
      dispatch(hideItem());
    };
  }, [dispatch]);

  return (
    <motion.div
      initial={{ scale: 0 }}
      animate={{ scale: isVisible ? 1 : 0 }}
      transition={{ duration: 0.5 }}
      className={clsx(
        'custom-bg p-6 sm:p-8 rounded-xl flex items-center justify-center space-y-8',
        className
      )}
      data-testid="item-layout"
    >
      {children}
    </motion.div>
  );
}

export default ItemLayoutComponent;
